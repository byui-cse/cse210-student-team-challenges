from game import director
import arcade 

def main():
    window = director.Director()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()