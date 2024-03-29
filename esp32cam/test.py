import requests

# Địa chỉ IP hoặc tên miền của ESP32-CAM
esp32_cam_ip = '192.168.1.16'
# Cổng mà web server của ESP32-CAM đang chạy
esp32_cam_port = 80

# URL để nhận ảnh từ ESP32-CAM
image_url = f'http://{esp32_cam_ip}:{esp32_cam_port}/capture'

def get_image_from_esp32_cam():
    try:
        # Gửi yêu cầu GET để nhận ảnh từ ESP32-CAM
        response = requests.get(image_url)
        # Lưu dữ liệu ảnh vào một file
        with open('captured_image.jpg', 'wb') as f:
            f.write(response.content)
        print("Đã lấy được ảnh từ ESP32-CAM")
    except requests.exceptions.RequestException as e:
        print("Lỗi khi gửi yêu cầu:", e)

# Gọi hàm để lấy ảnh từ ESP32-CAM
get_image_from_esp32_cam()
