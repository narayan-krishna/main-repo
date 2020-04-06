shot_list = []

class Test:
    def __init__(self, one, two):
        self.one = one
        self.two = two



# class Shot:
#     def __init__(self, number, date, previs, animation, effects, rendering, comp, done):
#         self.number = number
#         self.date = date
#         self.previs = previs
#         self.animation = animation
#         self.effects = effects
#         self.rendering = rendering
#         self.comp = comp
#         self.done = done
#
# def add_shot():
#     number = int(input("enter shot number: "))
#     date = input("input date to finish: ")
#     animation = input("animated: ")
#     effects = input("effects: ")
#     rendering = input("rendering: ")
#     comp = input("comp: ")
#     done = input("done: ")
#
#     shot = Shot(number, date, animation, effects, rendering, comp, done)
#     shot_list.append(shot)
#     shot_list.sort(key = lambda c: c.number)

add_shot()
