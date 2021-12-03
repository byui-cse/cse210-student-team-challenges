from game import kablam
import arcade 

def main():
    window = kablam.KablamGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()