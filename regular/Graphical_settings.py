class Graphical_settings:
    def __init__(self, option='basic'):
        option = option.upper()

        if option == 'VERTICAL_HD':
            self.MARGIN_LEFT = 75
            self.MARGIN_TOP = 150
            self.PADDING = 60
            self.VECTOR_SCALE = 50
            self.VECTOR_TIP_SIZE = 5
            self.WIDTH, self.HEIGHT = 1360, 768
            self.HORIZONTAL = False

        elif option == 'HORIZONTAL_HD':
            self.MARGIN_LEFT = 500
            self.MARGIN_TOP = 5
            self.PADDING = 37
            self.VECTOR_SCALE = 25
            self.VECTOR_TIP_SIZE = 3
            self.WIDTH, self.HEIGHT = 1360, 768
            self.HORIZONTAL = True

        elif option == 'VERTICAL_SMALL':
            self.MARGIN_LEFT = 50
            self.MARGIN_TOP = 50
            self.PADDING = 25
            self.VECTOR_SCALE = 17
            self.VECTOR_TIP_SIZE = 2
            self.WIDTH, self.HEIGHT = 600, 300
            self.HORIZONTAL = False

        elif option == 'HORIZONTAL_SMALL':
            self.MARGIN_LEFT = 50
            self.MARGIN_TOP = 50
            self.PADDING = 25
            self.VECTOR_SCALE = 17
            self.VECTOR_TIP_SIZE = 2
            self.WIDTH, self.HEIGHT = 300, 600
            self.HORIZONTAL = True

        elif option == 'BASIC':
            self.MARGIN_LEFT = 250
            self.MARGIN_TOP = 30
            self.PADDING = 40
            self.VECTOR_SCALE = 25
            self.VECTOR_TIP_SIZE = 3
            self.WIDTH, self.HEIGHT = 900, 900
            self.HORIZONTAL = True

        # Custom
        else:
            self.MARGIN_LEFT = 50
            self.MARGIN_TOP = 50
            self.PADDING = 25
            self.VECTOR_SCALE = 17
            self.VECTOR_TIP_SIZE = 2
            self.WIDTH, self.HEIGHT = 600, 300
            self.HORIZONTAL = False
