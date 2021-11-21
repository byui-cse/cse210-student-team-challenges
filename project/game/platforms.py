import random
import arcade
import time

class Platforms:

    def make_platforms(width, skyline_height, skyline_color,
                    gap_chance=0.70, window_chance=0.30, light_on_chance=0.5,
                    window_color=(255, 255, 200), window_margin=3, window_gap=2,
                    cap_chance=0.20):
        """ Make platforms """

        shape_list = arcade.ShapeElementList()

        # Add the "base" that we build the buildings on
        shape = arcade.create_rectangle_filled(width / 2, skyline_height / 2, width, skyline_height, skyline_color)
        shape_list.append(shape)

        building_center_x = 0

        skyline_point_list = []
        color_list = []

        while building_center_x < width:

            # Is there a gap between the buildings?
            if random.random() < gap_chance:
                gap_width = random.randrange(100, 200)
            else:
                gap_width = 0

            # Figure out location and size of building
            building_width = random.randrange(150, 300)
            building_height = random.randrange(40, 300)
            building_center_x += gap_width + (building_width / 2)
            building_center_y = skyline_height + (building_height / 2)

            x1 = building_center_x - building_width / 2
            x2 = building_center_x + building_width / 2
            y1 = skyline_height
            y2 = skyline_height + building_height

            skyline_point_list.append([x1, y1])

            skyline_point_list.append([x1, y2])

            skyline_point_list.append([x2, y2])

            skyline_point_list.append([x2, y1])

            for i in range(4):
                color_list.append([skyline_color[0], skyline_color[1], skyline_color[2]])

            if random.random() < cap_chance:
                x1 = building_center_x - building_width / 2
                x2 = building_center_x + building_width / 2
                x3 = building_center_x

                y1 = y2 = building_center_y + building_height / 2
                y3 = y1 + building_width / 2

                shape = arcade.create_polygon([[x1, y1], [x2, y2], [x3, y3]], skyline_color)
                shape_list.append(shape)

            # See if we should have some windows
            if random.random() < window_chance:
                # Yes windows! How many windows?
                window_rows = random.randrange(10, 15)
                window_columns = random.randrange(1, 7)

                # Based on that, how big should they be?
                window_height = (building_height - window_margin * 2) / window_rows
                window_width = (building_width - window_margin * 2 - window_gap * (window_columns - 1)) / window_columns

                # Find the bottom left of the building so we can start adding widows
                building_base_y = building_center_y - building_height / 2
                building_left_x = building_center_x - building_width / 2

                # Use this later to embellish the platforms, ruled out for now.
                # Loop through each window
                # for row in range(window_rows):
                #     for column in range(window_columns):
                #         if random.random() < light_on_chance:
                #             x1 = building_left_x + column * (window_width + window_gap) + window_margin
                #             x2 = building_left_x + column * (window_width + window_gap) + window_width + window_margin
                #             y1 = building_base_y + row * window_height
                #             y2 = building_base_y + row * window_height + window_height * .8

                #             skyline_point_list.append([x1, y1])
                #             skyline_point_list.append([x1, y2])
                #             skyline_point_list.append([x2, y2])
                #             skyline_point_list.append([x2, y1])

                #             for i in range(4):
                #                 color_list.append((window_color[0], window_color[1], window_color[2]))

            building_center_x += (building_width / 2)

        shape = arcade.create_rectangles_filled_with_colors(skyline_point_list, color_list)
        shape_list.append(shape)

        return shape_list