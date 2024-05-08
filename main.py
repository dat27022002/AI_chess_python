import pygame as p
import ChessMain

# Kích thước màn hình
SCREEN_WIDTH = 762
SCREEN_HEIGHT = 512

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Hàm vẽ nút
def draw_button(screen, color, rect, text):
    p.draw.rect(screen, color, rect)  # Vẽ nút
    font = p.font.Font(None, 36)  # Chọn font chữ
    text_surface = font.render(text, True, BLACK)  # Tạo text cho nút
    text_rect = text_surface.get_rect(center=rect.center)  # Định vị text trên nút
    screen.blit(text_surface, text_rect)  # Vẽ text trên nút

# Hàm chính
def main():
    p.init()  # Khởi tạo Pygame
    p.display.set_caption("Chess Game")
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Tạo màn hình
    running = True
    
    # Tải hình ảnh nền
    background_image = p.image.load("bg.jpg")
    background_rect = background_image.get_rect()
        
    # Định nghĩa các nút
    button_width = 100  # Chiều rộng nút
    button_height = 50  # Chiều cao nút
    button_spacing = 20  # Khoảng cách giữa các nút
    
    # Tính toán vị trí giữa màn hình theo chiều ngang
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Đặt các nút ở giữa màn hình, với khoảng cách giữa chúng
    easy_btn = p.Rect(center_x - (1.5 * (button_width + button_spacing)), center_y, button_width, button_height)
    normal_btn = p.Rect(center_x - (0.5 * (button_width + button_spacing)), center_y, button_width, button_height)
    hard_btn = p.Rect(center_x + (0.5 * (button_width + button_spacing)), center_y, button_width, button_height)

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:  # Thoát khi nhấn nút đóng cửa sổ
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:  # Xử lý nhấp chuột
                if easy_btn.collidepoint(event.pos):
                    ChessMain.main(1)
                    print("Easy mode selected")  # Gọi hàm hoặc thiết lập cho easy mode
                elif normal_btn.collidepoint(event.pos):
                    ChessMain.main(2)
                    print("Normal mode selected")  # Gọi hàm hoặc thiết lập cho normal mode
                elif hard_btn.collidepoint(event.pos):
                    ChessMain.main(3)
                    print("Hard mode selected")  # Gọi hàm hoặc thiết lập cho hard mode

        # Vẽ nền trắng
        screen.blit(background_image, background_rect)

        # Vẽ ba nút
        draw_button(screen, GREEN, easy_btn, "Easy")
        draw_button(screen, YELLOW, normal_btn, "Normal")
        draw_button(screen, RED, hard_btn, "Hard")

        # Cập nhật màn hình
        p.display.flip()

    p.quit()  # Thoát Pygame

if __name__ == "__main__":
    main()