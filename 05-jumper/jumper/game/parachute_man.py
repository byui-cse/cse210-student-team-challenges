class Parachute_man:
   def __init__(self):
      self.parachute_beg = "  ___\n /___\ \n \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
      self.parachute1 = "\n /___\ \n \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
      self.parachute2 = "\n\n \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
      self.parachute3 = "\n\n\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
      self.parachute_dead = "\n\n\n\n   X\n  /|\ \n  / \ \n\n^^^^^^^"

   def para_display(self, wrong):
      if wrong == 0:
         return self.parachute_beg
      elif wrong == 1:
         return self.parachute1
      elif wrong == 2:
         return self.parachute2
      elif wrong == 3:
         return self.parachute3
      elif wrong == 4:
         return self.parachute_dead