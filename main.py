from PIL import Image
from ultralytics import YOLO
import requests
from io import BytesIO
from PIL import Image

# Địa chỉ IP hoặc tên miền của ESP32-CAM
esp32_cam_ip = '192.168.1.171'
# Cổng mà web server của ESP32-CAM đang chạy
esp32_cam_port = 80

# URL để nhận ảnh từ ESP32-CAM
image_url = f'http://{esp32_cam_ip}:{esp32_cam_port}/capture'

def detect_objects_in_image(image_bytes):
    # Khởi tạo mô hình YOLO
    yolo = YOLO(r"yolov8\LeafDetetion3\weights\best.pt")

    # Chuyển đổi dữ liệu ảnh từ bytes thành đối tượng Image
    image = Image.open(BytesIO(image_bytes))

    # Nhận diện các đối tượng trong ảnh
    results = yolo.predict(image, save=True)
    print(results)

def get_image_from_esp32_cam():
    try:
        # Gửi yêu cầu GET để nhận ảnh từ ESP32-CAM
        response = requests.get(image_url)
        with open("leaf.jpg", 'wb') as f:
            f.write(response.content)
        print(type(response.content))
        print(response.content)
        # Gọi hàm để nhận diện các đối tượng trong ảnh
        detect_objects_in_image(response.content)
        print("Đã nhận diện các đối tượng trong ảnh từ ESP32-CAM")
    except requests.exceptions.RequestException as e:
        print("Lỗi khi gửi yêu cầu:", e)

# Gọi hàm để lấy và nhận diện ảnh từ ESP32-CAM
get_image_from_esp32_cam()
