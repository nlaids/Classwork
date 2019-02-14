import arcade


WIDTH = 640
HEIGHT = 480

x = int(input('Please enter x :'))
y = int(input('Please enter y :'))
radius = int(input('Please enter radius :'))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.ALABAMA_CRIMSON)

# End drawing
arcade.finish_render()
arcade.run()