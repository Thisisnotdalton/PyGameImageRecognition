import pygame


class App:
    def __init__(self, width=1280, height=720, frame_rate=120, name='My Pygame App'):
        pygame.init()
        self.screen_res = (width, height)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(size=self.screen_res)
        pygame.display.set_caption(name)
        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.draw()
            self.clock.tick(self.frame_rate)

    def on_event(self, event: pygame.event.EventType):
        if event.type == pygame.QUIT:
            self.running = False

    def draw(self):
        pygame.display.flip()


class DrawingApp(App):
    def __init__(self, width=1280, height=720, background_color=pygame.Color(255, 255, 255), ui_color=pygame.Color(127, 127, 127),
                 draw_color=pygame.Color(0, 0, 0), brush_size=20, canvas_width=720, canvas_height=720):
        super().__init__(width=width, height=height, name='Drawing App')
        self.background_color = background_color
        self.draw_color = draw_color
        self.ui_color=ui_color
        self.brush_size = brush_size
        self.drawing = False
        self.canvas = pygame.Surface((canvas_width, canvas_height))
        self.canvas_position = (int((width - canvas_width)/2), int((height - canvas_height)/2))
        self.canvas.fill(self.background_color)
        self.last_mouse_position = None

    def on_event(self, event: pygame.event.EventType):
        super().on_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False

    def draw(self):
        self.screen.fill(self.ui_color)
        mouse_position = pygame.mouse.get_pos()
        canvas_mouse_position = mouse_position[0] - self.canvas_position[0], mouse_position[1] - self.canvas_position[1]
        if 0 <= canvas_mouse_position[0] <= self.canvas.get_width() and 0 <= canvas_mouse_position[1] <= self.canvas.get_height():
            if self.drawing:
                pygame.draw.circle(self.canvas, self.draw_color, canvas_mouse_position, int(self.brush_size / 2))
                if self.last_mouse_position is not None:
                    pygame.draw.line(self.canvas, self.draw_color, self.last_mouse_position,
                                     canvas_mouse_position, self.brush_size)
            self.last_mouse_position = canvas_mouse_position

        self.screen.blit(self.canvas, self.canvas_position)
        super().draw()


if __name__ == '__main__':
    app = DrawingApp()
    app.run()
