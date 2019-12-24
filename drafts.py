from tkinter import *
import copy
import random


root = Tk()




class MenuScreen:

    def __init__(self):
        self.menu = Frame(width=300 * board.size, height=300 * board.size, bg="light blue")
        self.menu.pack(fill="x", padx=50, pady=10)

        self.play1 = Button(self.menu, text="1 Player", command=board.startgame1, height=int(3 * board.size),
                            width=int(30 * board.size), bg="light blue")
        self.play1.pack(fill="x", padx=50, pady=10)

        self.play2 = Button(self.menu, text="2 Player", command=board.startgame2, height=int(3 * board.size),
                            width=int(30 * board.size), bg="light blue")
        self.play2.pack(fill="x", padx=50, pady=10)

    def openmenu(self):
        pannel.pannel.destroy()
        root.unbind("<Button-1>", board.cl)
        menu.__init__()


class GameBoard:

    def __init__(self, size):
        self.size = size

    def startgame1(self):
        menu.menu.destroy()
        self.mode = 1
        pannel.run()
        self.run()

    def startgame2(self):
        menu.menu.destroy()
        self.mode = 2
        pannel.run()
        self.run()

    def showounternums(self, d):
        if d == True:
            for x in range(0, 8):
                for y in range(0, 8):
                    if board.grid[y][x] != "_":
                        if board.grid[y][x] == 1:
                            self.i1 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 2:
                            self.i2 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")
                        elif board.grid[y][x] == 3:
                            self.i3 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 4:
                            self.i4 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 5:
                            self.i5 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 6:
                            self.i6 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 7:
                            self.i7 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 8:
                            self.i8 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 9:
                            self.i9 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                           (y * 50 * self.size) + (25 * self.size),
                                                           text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 10:
                            self.i10 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 11:
                            self.i11 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 12:
                            self.i12 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}")

                        elif board.grid[y][x] == 13:
                            self.i13 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 14:
                            self.i14 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 15:
                            self.i15 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 16:
                            self.i16 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 17:
                            self.i17 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 18:
                            self.i18 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 19:
                            self.i19 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 20:
                            self.i20 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 21:
                            self.i21 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 22:
                            self.i22 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 23:
                            self.i23 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

                        elif board.grid[y][x] == 24:
                            self.i24 = pannel.c.create_text((x * 50 * self.size) + (25 * self.size),
                                                            (y * 50 * self.size) + (25 * self.size),
                                                            text=f"{board.grid[y][x]}", fill="white")

        else:
            pannel.c.delete(self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.i9, self.i10,
                            self.i11, self.i12, self.i13, self.i14, self.i15, self.i16, self.i17, self.i18, self.i19,
                            self.i20, self.i21, self.i22, self.i23, self.i24)

            pannel.c.update()

    def run(self):
        self.turn = "black"
        self.drawgrid()
        self.layoutcounters()
        self.count()
        self.cl = root.bind("<Button-1>", board.click)
        self.triplejumping = True
        self.repbutton()

    def drawgrid(self):

        row = "o"
        for a in range(0, 8):
            if row == "o":
                row = "e"
            elif row == "e":
                row = "o"
            for i in range(0, 4):
                if row == "e":
                    pannel.c.create_rectangle((i * 100 * self.size), (a * 50 * self.size),
                                              (i * 100 * self.size) + 50 * self.size,
                                              (a * 50 * self.size) + 50 * self.size,
                                              fill="light grey")
                    pannel.c.create_rectangle((i * 100 * self.size) + 50 * self.size, (a * 50 * self.size),
                                              (i * 100 * self.size) + 100 * self.size,
                                              (a * 50 * self.size) + 50 * self.size,
                                              fill="dark grey")
                elif row == "o":
                    pannel.c.create_rectangle((i * 100 * self.size), (a * 50 * self.size),
                                              (i * 100 * self.size) + 50 * self.size,
                                              (a * 50 * self.size) + 50 * self.size,
                                              fill="dark grey")
                    pannel.c.create_rectangle((i * 100 * self.size) + 50 * self.size, (a * 50 * self.size),
                                              (i * 100 * self.size) + 100 * self.size,
                                              (a * 50 * self.size) + 50 * self.size,
                                              fill="light grey")

    def layoutcounters(self):
        global grid
        self.selecting = False
        self.counter13 = Counter("black", False, 0, 1, 13)
        self.counter14 = Counter("black", False, 0, 3, 14)
        self.counter15 = Counter("black", False, 0, 5, 15)
        self.counter16 = Counter("black", False, 0, 7, 16)
        self.counter17 = Counter("black", False, 1, 0, 17)
        self.counter18 = Counter("black", False, 1, 2, 18)
        self.counter19 = Counter("black", False, 1, 4, 19)
        self.counter20 = Counter("black", False, 1, 6, 20)
        self.counter21 = Counter("black", False, 2, 1, 21)
        self.counter22 = Counter("black", False, 2, 3, 22)
        self.counter23 = Counter("black", False, 2, 5, 23)
        self.counter24 = Counter("black", False, 2, 7, 24)

        self.counter01 = Counter("white", False, 5, 0, 1)
        self.counter02 = Counter("white", False, 5, 2, 2)
        self.counter03 = Counter("white", False, 5, 4, 3)
        self.counter04 = Counter("white", False, 5, 6, 4)
        self.counter05 = Counter("white", False, 6, 1, 5)
        self.counter06 = Counter("white", False, 6, 3, 6)
        self.counter07 = Counter("white", False, 6, 5, 7)
        self.counter08 = Counter("white", False, 6, 7, 8)
        self.counter09 = Counter("white", False, 7, 0, 9)
        self.counter10 = Counter("white", False, 7, 2, 10)
        self.counter11 = Counter("white", False, 7, 4, 11)
        self.counter12 = Counter("white", False, 7, 6, 12)

        self.grid = [[] * 8]
        self.grid *= 0
        self.grid.append(
            ["_", self.counter13.num, "_", self.counter14.num, "_", self.counter15.num, "_", self.counter16.num])
        self.grid.append(
            [self.counter17.num, "_", self.counter18.num, "_", self.counter19.num, "_", self.counter20.num, "_"])
        self.grid.append(
            ["_", self.counter21.num, "_", self.counter22.num, "_", self.counter23.num, "_", self.counter24.num])
        self.grid.append(["_", "_", "_", "_", "_", "_", "_", "_"])
        self.grid.append(["_", "_", "_", "_", "_", "_", "_", "_"])
        self.grid.append(
            [self.counter01.num, "_", self.counter02.num, "_", self.counter03.num, "_", self.counter04.num, "_"])
        self.grid.append(
            ["_", self.counter05.num, "_", self.counter06.num, "_", self.counter07.num, "_", self.counter08.num])
        self.grid.append(
            [self.counter09.num, "_", self.counter10.num, "_", self.counter11.num, "_", self.counter12.num, "_"])

    def click(self, event):

        across = int(pannel.c.canvasx(event.x) / (50 * self.size))
        down = int(pannel.c.canvasy(event.y) / (50 * self.size))

        if across > -1 and across < 8 and down > -1 and down < 8:
            if self.selecting == False:

                if self.grid[down][across] != "_":
                    if self.grid[down][across] == self.counter01.num:
                        self.counter01.click()
                    elif self.grid[down][across] == self.counter02.num:
                        self.counter02.click()
                    elif self.grid[down][across] == self.counter03.num:
                        self.counter03.click()
                    elif self.grid[down][across] == self.counter04.num:
                        self.counter04.click()
                    elif self.grid[down][across] == self.counter05.num:
                        self.counter05.click()
                    elif self.grid[down][across] == self.counter06.num:
                        self.counter06.click()
                    elif self.grid[down][across] == self.counter07.num:
                        self.counter07.click()
                    elif self.grid[down][across] == self.counter08.num:
                        self.counter08.click()
                    elif self.grid[down][across] == self.counter09.num:
                        self.counter09.click()
                    elif self.grid[down][across] == self.counter10.num:
                        self.counter10.click()
                    elif self.grid[down][across] == self.counter11.num:
                        self.counter11.click()
                    elif self.grid[down][across] == self.counter12.num:
                        self.counter12.click()
                    elif self.grid[down][across] == self.counter13.num:
                        self.counter13.click()
                    elif self.grid[down][across] == self.counter14.num:
                        self.counter14.click()
                    elif self.grid[down][across] == self.counter15.num:
                        self.counter15.click()
                    elif self.grid[down][across] == self.counter16.num:
                        self.counter16.click()
                    elif self.grid[down][across] == self.counter17.num:
                        self.counter17.click()
                    elif self.grid[down][across] == self.counter18.num:
                        self.counter18.click()
                    elif self.grid[down][across] == self.counter19.num:
                        self.counter19.click()
                    elif self.grid[down][across] == self.counter20.num:
                        self.counter20.click()
                    elif self.grid[down][across] == self.counter21.num:
                        self.counter21.click()
                    elif self.grid[down][across] == self.counter22.num:
                        self.counter22.click()
                    elif self.grid[down][across] == self.counter23.num:
                        self.counter23.click()
                    elif self.grid[down][across] == self.counter24.num:
                        self.counter24.click()
            else:
                if self.c_selecting == 1:
                    self.counter01.move(across, down)
                elif self.c_selecting == 2:
                    self.counter02.move(across, down)
                elif self.c_selecting == 3:
                    self.counter03.move(across, down)
                elif self.c_selecting == 4:
                    self.counter04.move(across, down)
                elif self.c_selecting == 5:
                    self.counter05.move(across, down)
                elif self.c_selecting == 6:
                    self.counter06.move(across, down)
                elif self.c_selecting == 7:
                    self.counter07.move(across, down)
                elif self.c_selecting == 8:
                    self.counter08.move(across, down)
                elif self.c_selecting == 9:
                    self.counter09.move(across, down)
                elif self.c_selecting == 10:
                    self.counter10.move(across, down)
                elif self.c_selecting == 11:
                    self.counter11.move(across, down)
                elif self.c_selecting == 12:
                    self.counter12.move(across, down)
                elif self.c_selecting == 13:
                    self.counter13.move(across, down)
                elif self.c_selecting == 14:
                    self.counter14.move(across, down)
                elif self.c_selecting == 15:
                    self.counter15.move(across, down)
                elif self.c_selecting == 16:
                    self.counter16.move(across, down)
                elif self.c_selecting == 17:
                    self.counter17.move(across, down)
                elif self.c_selecting == 18:
                    self.counter18.move(across, down)
                elif self.c_selecting == 19:
                    self.counter19.move(across, down)
                elif self.c_selecting == 20:
                    self.counter20.move(across, down)
                elif self.c_selecting == 21:
                    self.counter21.move(across, down)
                elif self.c_selecting == 22:
                    self.counter22.move(across, down)
                elif self.c_selecting == 23:
                    self.counter23.move(across, down)
                elif self.c_selecting == 24:
                    self.counter24.move(across, down)

    def count(self):

        self.WhiteCounters = 0
        self.BlackCounters = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.grid[y][x] != "_":
                    temp = self.grid[y][x] - 12
                    if temp <= 0:
                        self.WhiteCounters = self.WhiteCounters + 1

                    else:
                        self.BlackCounters = self.BlackCounters + 1
        if self.BlackCounters == 0:
            pannel.c.update()
            root.after(1000, self.win("W"))
        elif self.WhiteCounters == 0:
            pannel.c.update()
            root.after(1000, self.win("B"))

        pannel.whitesLabel.config(text="White Counters: {}".format(self.WhiteCounters))
        pannel.blacksLabel.config(text="Black Counters: {}".format(self.BlackCounters))

    def kill(self, target, killx1, killx2, killy1, killy2, killx3, killx4, killy3, killy4):

        if target == "A":
            X = killx1
            Y = killy1
        elif target == "B":
            X = killx2
            Y = killy2
        elif target == "C":
            X = killx3
            Y = killy3
        elif target == "D":
            X = killx4
            Y = killy4
        # print(X, Y)
        # print(self.grid[X][Y])
        if self.grid[X][Y] == 1:
            pannel.c.delete(self.counter01.oval)

        elif self.grid[X][Y] == 2:
            pannel.c.delete(self.counter02.oval)

        elif self.grid[X][Y] == 3:
            pannel.c.delete(self.counter03.oval)

        elif self.grid[X][Y] == 4:
            pannel.c.delete(self.counter04.oval)

        elif self.grid[X][Y] == 5:
            pannel.c.delete(self.counter05.oval)

        elif self.grid[X][Y] == 6:
            pannel.c.delete(self.counter06.oval)

        elif self.grid[X][Y] == 7:
            pannel.c.delete(self.counter07.oval)

        elif self.grid[X][Y] == 8:
            pannel.c.delete(self.counter08.oval)

        elif self.grid[X][Y] == 9:
            pannel.c.delete(self.counter09.oval)

        elif self.grid[X][Y] == 10:
            pannel.c.delete(self.counter10.oval)

        elif self.grid[X][Y] == 11:
            pannel.c.delete(self.counter11.oval)

        elif self.grid[X][Y] == 12:
            pannel.c.delete(self.counter12.oval)

        elif self.grid[X][Y] == 13:
            pannel.c.delete(self.counter13.oval)

        elif self.grid[X][Y] == 14:
            pannel.c.delete(self.counter14.oval)

        elif self.grid[X][Y] == 15:
            pannel.c.delete(self.counter15.oval)

        elif self.grid[X][Y] == 16:
            pannel.c.delete(self.counter16.oval)

        elif self.grid[X][Y] == 17:
            pannel.c.delete(self.counter17.oval)

        elif self.grid[X][Y] == 18:
            pannel.c.delete(self.counter18.oval)

        elif self.grid[X][Y] == 19:
            pannel.c.delete(self.counter19.oval)

        elif self.grid[X][Y] == 20:
            pannel.c.delete(self.counter20.oval)

        elif self.grid[X][Y] == 21:
            pannel.c.delete(self.counter21.oval)

        elif self.grid[X][Y] == 22:
            pannel.c.delete(self.counter22.oval)

        elif self.grid[X][Y] == 23:
            pannel.c.delete(self.counter23.oval)

        elif self.grid[X][Y] == 24:
            pannel.c.delete(self.counter24.oval)

        self.grid[X][Y] = "_"
        Ai.getscore(self.grid)

    def win(self, winner):
        global replay
        pannel.c.delete("all")
        if winner == "B":

            pannel.c.configure(bg="black")
            pannel.c.create_text(200 * self.size, 200 * self.size, fill="white", font=("Verdana", 25),
                                 text="Blacks won the game!")
            pannel.c.create_text(200 * self.size, 300 * self.size, fill="white", font=("Verdana", 20),
                                 text="[Press enter play again]")
            pannel.c.create_rectangle(30 * self.size, 30 * self.size, 370 * self.size, 370 * self.size, outline="white",
                                      width=10 * self.size)
        elif winner == "W":
            pannel.c.configure(bg="white")
            pannel.c.create_text(200 * self.size, 200 * self.size, fill="black", font=("Verdana", 25),
                                 text="Whites won the game!")
            pannel.c.create_text(200 * self.size, 300 * self.size, fill="black", font=("Verdana", 20),
                                 text="[Press enter play again]")
            pannel.c.create_rectangle(30 * self.size, 30 * self.size, 370 * self.size, 370 * self.size, outline="black",
                                      width=10 * self.size)
        elif winner == "D":
            pannel.c.configure(bg="green")
            pannel.c.create_text(200 * self.size, 200 * self.size, fill="white", font=("Verdana", 25),
                                 text="It's a Draw!")
            pannel.c.create_text(200 * self.size, 300 * self.size, fill="white", font=("Verdana", 20),
                                 text="[Press enter play again]")
            pannel.c.create_rectangle(30 * self.size, 30 * self.size, 370 * self.size, 370 * self.size, outline="white",
                                      width=10 * self.size)
        replay = root.bind("<Return>", self.rep)

    def rep(self, event):

        root.unbind("<Return>", replay)
        self.repbutton()

    def repbutton(self):

        pannel.c.configure(bg="white")
        pannel.c.delete("all")

        self.grid *= 0
        self.grid.append(
            ["_", self.counter13.num, "_", self.counter14.num, "_", self.counter15.num, "_", self.counter16.num])
        self.grid.append(
            [self.counter17.num, "_", self.counter18.num, "_", self.counter19.num, "_", self.counter20.num, "_"])
        self.grid.append(
            ["_", self.counter21.num, "_", self.counter22.num, "_", self.counter23.num, "_", self.counter24.num])
        self.grid.append(["_", "_", "_", "_", "_", "_", "_", "_"])
        self.grid.append(["_", "_", "_", "_", "_", "_", "_", "_"])
        self.grid.append(
            [self.counter01.num, "_", self.counter02.num, "_", self.counter03.num, "_", self.counter04.num, "_"])
        self.grid.append(
            ["_", self.counter05.num, "_", self.counter06.num, "_", self.counter07.num, "_", self.counter08.num])
        self.grid.append(
            [self.counter09.num, "_", self.counter10.num, "_", self.counter11.num, "_", self.counter12.num, "_"])
        self.drawgrid()
        self.turn = "white"
        self.triplejumping = False
        self.selecting = False
        self.counter13.__init__("black", False, 0, 1, 13)
        self.counter14.__init__("black", False, 0, 3, 14)
        self.counter15.__init__("black", False, 0, 5, 15)
        self.counter16.__init__("black", False, 0, 7, 16)
        self.counter17.__init__("black", False, 1, 0, 17)
        self.counter18.__init__("black", False, 1, 2, 18)
        self.counter19.__init__("black", False, 1, 4, 19)
        self.counter20.__init__("black", False, 1, 6, 20)
        self.counter21.__init__("black", False, 2, 1, 21)
        self.counter22.__init__("black", False, 2, 3, 22)
        self.counter23.__init__("black", False, 2, 5, 23)
        self.counter24.__init__("black", False, 2, 7, 24)

        self.counter01.__init__("white", False, 5, 0, 1)
        self.counter02.__init__("white", False, 5, 2, 2)
        self.counter03.__init__("white", False, 5, 4, 3)
        self.counter04.__init__("white", False, 5, 6, 4)
        self.counter05.__init__("white", False, 6, 1, 5)
        self.counter06.__init__("white", False, 6, 3, 6)
        self.counter07.__init__("white", False, 6, 5, 7)
        self.counter08.__init__("white", False, 6, 7, 8)
        self.counter09.__init__("white", False, 7, 0, 9)
        self.counter10.__init__("white", False, 7, 2, 10)
        self.counter11.__init__("white", False, 7, 4, 11)
        self.counter12.__init__("white", False, 7, 6, 12)

        self.count()

    def swapturn(self):
        if self.turn == "white":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "white"

    def checkfordraw(self):

        moveableblack, moveablewhite = Ai.countmoveablecounters(self.grid)
        if moveablewhite == []:
            white = False
        else:
            white = True
        if moveableblack == []:
            black = False
        else:
            black = True

        if self.turn == "white" and not white and black:
            board.swapturn()

        if self.turn == "black" and not black and white:
            board.swapturn()

        if not black and not white:
            self.calcdraw()

    def calcdraw(self):

        self.count()

        if self.BlackCounters < self.WhiteCounters:
            pannel.c.update()
            root.after(1000, self.win("W"))
        elif self.WhiteCounters < self.BlackCounters:
            pannel.c.update()
            root.after(1000, self.win("B"))
        else:
            pannel.c.update()
            root.after(1000, self.win("D"))

    def guidelines(self, clear):

        if clear:
            self.inplay *= 0
        else:
            if pannel.on:
                moveableblack, moveablewhite = Ai.countmoveablecounters(self.grid)
                if self.turn == "white":
                    self.inplay = copy.deepcopy(moveablewhite)
                else:
                    self.inplay = copy.deepcopy(moveableblack)
        self.counter01.createguideline()
        self.counter02.createguideline()
        self.counter03.createguideline()
        self.counter04.createguideline()
        self.counter05.createguideline()
        self.counter06.createguideline()
        self.counter07.createguideline()
        self.counter08.createguideline()
        self.counter09.createguideline()
        self.counter10.createguideline()
        self.counter11.createguideline()
        self.counter12.createguideline()
        self.counter13.createguideline()
        self.counter14.createguideline()
        self.counter15.createguideline()
        self.counter16.createguideline()
        self.counter17.createguideline()
        self.counter18.createguideline()
        self.counter19.createguideline()
        self.counter20.createguideline()
        self.counter21.createguideline()
        self.counter22.createguideline()
        self.counter23.createguideline()
        self.counter24.createguideline()


class Counter:

    def __init__(self, colour, double, x, y, number):
        self.colour = colour
        self.double = double
        self.x = x
        self.y = y
        self.A = False
        self.B = False
        self.C = False
        self.D = False
        self.Ad = False
        self.Bd = False
        self.Cd = False
        self.Dd = False
        self.num = number
        self.oval = pannel.c.create_oval((self.y * 50 * board.size) + 5 * board.size,
                                         (self.x * 50 * board.size) + 5 * board.size,
                                         ((self.y * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                         ((self.x * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                         fill=self.colour,
                                         width=1 * board.size)

    def click(self):
        if board.triplejumping == True:
            board.swapturn()
            board.triplejumping = False
            if board.mode == 1:
                Ai.aiturn()

            # Ai.aiturn()
        if self.colour == board.turn:

            if pannel.on:
                board.guidelines(True)
            pannel.c.itemconfigure(self.oval, outline="green", width=3 * board.size)
            if self.colour == "white":
                self.nx1 = (self.x - 1)
                self.nx2 = (self.x - 1)
                self.ny1 = (self.y - 1)
                self.ny2 = (self.y + 1)
                self.nx3 = (self.x + 1)
                self.nx4 = (self.x + 1)
                self.ny3 = (self.y - 1)
                self.ny4 = (self.y + 1)

            if self.colour == "black":
                self.nx1 = (self.x + 1)
                self.nx2 = (self.x + 1)
                self.ny1 = (self.y - 1)
                self.ny2 = (self.y + 1)
                self.nx3 = (self.x - 1)
                self.nx4 = (self.x - 1)
                self.ny3 = (self.y - 1)
                self.ny4 = (self.y + 1)

            self.Ad = False
            self.Bd = False
            self.Cd = False
            self.Dd = False
            self.checksingle()
            self.checkdouble()

            if self.A == False and self.B == False and self.C == False and self.D == False:
                pannel.c.itemconfigure(self.oval, outline="black", width=1 * board.size)
                if pannel.on:
                    board.guidelines(False)
        else:
            pannel.c.itemconfigure(self.oval, outline="red", width=3 * board.size)
            pannel.c.update()
            pannel.c.after(700, self.changeback())
            if board.triplejumping == True:
                board.swapturn()

    def changeback(self):
        pannel.c.itemconfigure(self.oval, outline="black", width=1 * board.size)

    def checksingle(self):

        if self.double:
            if self.colour == "white":
                if self.nx3 < 8 and self.ny3 > -1:
                    if board.grid[self.nx3][self.ny3] == "_":
                        if pannel.on:
                            self.optionC = pannel.c.create_oval((self.ny3 * 50 * board.size) + 5 * board.size,
                                                                (self.nx3 * 50 * board.size) + 5 * board.size,
                                                                ((
                                                                         self.ny3 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx3 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.C = True
                        board.selecting = True
                        board.c_selecting = self.num
                if self.nx4 < 8 and self.ny4 < 8:
                    if board.grid[self.nx4][self.ny4] == "_":
                        if pannel.on:
                            self.optionD = pannel.c.create_oval((self.ny4 * 50 * board.size) + 5 * board.size,
                                                                (self.nx4 * 50 * board.size) + 5 * board.size,
                                                                ((
                                                                         self.ny4 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx4 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.D = True
                        board.selecting = True
                        board.c_selecting = self.num

            if self.colour == "black":
                if self.nx3 > -1 and self.ny3 > -1:
                    if board.grid[self.nx3][self.ny3] == "_":
                        if pannel.on:
                            self.optionC = pannel.c.create_oval((self.ny3 * 50 * board.size) + 5 * board.size,
                                                                (self.nx3 * 50 * board.size) + 5 * board.size,
                                                                ((
                                                                         self.ny3 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx3 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.C = True
                        board.selecting = True
                        board.c_selecting = self.num

                if self.ny4 > -1 and self.ny4 < 8:
                    if board.grid[self.nx4][self.ny4] == "_":
                        if pannel.on:
                            self.optionD = pannel.c.create_oval((self.ny4 * 50 * board.size) + 5 * board.size,
                                                                (self.nx4 * 50 * board.size) + 5 * board.size,
                                                                ((
                                                                         self.ny4 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx4 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.D = True
                        board.selecting = True
                        board.c_selecting = self.num

        if self.colour == "white":
            if self.nx1 > -1 and self.ny1 > -1:
                if board.grid[self.nx1][self.ny1] == "_":
                    if pannel.on:
                        self.optionA = pannel.c.create_oval((self.ny1 * 50 * board.size) + 5 * board.size,
                                                            (self.nx1 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny1 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx1 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.A = True
                    board.selecting = True
                    board.c_selecting = self.num

            if self.ny2 > -1 and self.ny2 < 8:
                if board.grid[self.nx2][self.ny2] == "_":
                    if pannel.on:
                        self.optionB = pannel.c.create_oval((self.ny2 * 50 * board.size) + 5 * board.size,
                                                            (self.nx2 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny2 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx2 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.B = True
                    board.selecting = True
                    board.c_selecting = self.num

        if self.colour == "black":

            if self.nx1 < 8 and self.ny1 > -1:
                if board.grid[self.nx1][self.ny1] == "_":
                    if pannel.on:
                        self.optionA = pannel.c.create_oval((self.ny1 * 50 * board.size) + 5 * board.size,
                                                            (self.nx1 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny1 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx1 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.A = True
                    board.selecting = True
                    board.c_selecting = self.num
            if self.nx2 < 8 and self.ny2 < 8:
                if board.grid[self.nx2][self.ny2] == "_":
                    if pannel.on:
                        self.optionB = pannel.c.create_oval((self.ny2 * 50 * board.size) + 5 * board.size,
                                                            (self.nx2 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny2 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx2 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.B = True
                    board.selecting = True
                    board.c_selecting = self.num

    def checkdouble(self):

        self.killx1 = 0
        self.killx2 = 0
        self.killy1 = 0
        self.killy2 = 0
        self.killx3 = 0
        self.killx4 = 0
        self.killy3 = 0
        self.killy4 = 0
        if self.colour == "black":
            if (self.nx1 + 1) < 8 and (self.ny1 - 1) > -1 and self.nx1 < 8 and self.ny1 > -1:
                if (board.grid[self.nx1][self.ny1] == 1 or board.grid[self.nx1][self.ny1] == 2 or board.grid[self.nx1][
                    self.ny1] == 3 or \
                    board.grid[self.nx1][self.ny1] == 4 or board.grid[self.nx1][self.ny1] == 5 or board.grid[self.nx1][
                        self.ny1] == 6 or \
                    board.grid[self.nx1][self.ny1] == 7 or board.grid[self.nx1][self.ny1] == 8 or board.grid[self.nx1][
                        self.ny1] == 9 or \
                    board.grid[self.nx1][self.ny1] == 10 or board.grid[self.nx1][self.ny1] == 11 or
                    board.grid[self.nx1][self.ny1] == 12) \
                        and (board.grid[self.nx1 + 1][self.ny1 - 1] == "_") and self.A == False:
                    self.killx1 = self.nx1
                    self.killy1 = self.ny1
                    self.nx1 = self.nx1 + 1
                    self.ny1 = self.ny1 - 1
                    if pannel.on:
                        self.optionA = pannel.c.create_oval((self.ny1 * 50 * board.size) + 5 * board.size,
                                                            (self.nx1 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny1 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx1 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.A = True
                    self.Ad = True
                    board.selecting = True
                    board.c_selecting = self.num
            if (self.nx2 + 1) < 8 and (self.ny2 + 1) < 8 and self.nx2 < 8 and self.ny2 < 8:
                if (board.grid[self.nx2][self.ny2] == 1 or board.grid[self.nx2][self.ny2] == 2 or board.grid[self.nx2][
                    self.ny2] == 3 or \
                    board.grid[self.nx2][self.ny2] == 4 or board.grid[self.nx2][self.ny2] == 5 or board.grid[self.nx2][
                        self.ny2] == 6 or \
                    board.grid[self.nx2][self.ny2] == 7 or board.grid[self.nx2][self.ny2] == 8 or board.grid[self.nx2][
                        self.ny2] == 9 or \
                    board.grid[self.nx2][self.ny2] == 10 or board.grid[self.nx2][self.ny2] == 11 or
                    board.grid[self.nx2][self.ny2] == 12) \
                        and (board.grid[self.nx2 + 1][self.ny2 + 1] == "_") and self.B == False:
                    self.killx2 = self.nx2
                    self.killy2 = self.ny2
                    self.nx2 = self.nx2 + 1
                    self.ny2 = self.ny2 + 1
                    if pannel.on:
                        self.optionB = pannel.c.create_oval((self.ny2 * 50 * board.size) + 5 * board.size,
                                                            (self.nx2 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny2 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx2 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.Bd = True
                    self.B = True
                    board.selecting = True
                    board.c_selecting = self.num

            if self.double:

                if (self.nx3 - 1) > -1 and (self.ny3 - 1) > -1 and self.nx3 > -1 and self.ny3 > -1:
                    if (board.grid[self.nx3][self.ny3] == 1 or board.grid[self.nx3][self.ny3] == 2 or
                        board.grid[self.nx3][self.ny3] == 3 or \
                        board.grid[self.nx3][self.ny3] == 4 or board.grid[self.nx3][self.ny3] == 5 or
                        board.grid[self.nx3][self.ny3] == 6 or \
                        board.grid[self.nx3][self.ny3] == 7 or board.grid[self.nx3][self.ny3] == 8 or
                        board.grid[self.nx3][self.ny3] == 9 or \
                        board.grid[self.nx3][self.ny3] == 10 or board.grid[self.nx3][self.ny3] == 11 or
                        board.grid[self.nx3][self.ny3] == 12) \
                            and (board.grid[self.nx3 - 1][self.ny3 - 1] == "_") and self.C == False:
                        self.killx3 = self.nx3
                        self.killy3 = self.ny3
                        self.nx3 = self.nx3 - 1
                        self.ny3 = self.ny3 - 1
                        if pannel.on:
                            self.optionC = pannel.c.create_oval((self.ny3 * 50 * board.size) + 5 * board.size,
                                                                (self.nx3 * 50 * board.size) + 5 * board.size, ((
                                                                                                                        self.ny3 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx3 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.C = True
                        self.Cd = True
                        board.selecting = True
                        board.c_selecting = self.num
                if (self.nx4 - 1) != -1 and (self.ny4 + 1) != 8 and self.ny4 != -1 and self.ny4 != 8:
                    if (board.grid[self.nx4][self.ny4] == 1 or board.grid[self.nx4][self.ny4] == 2 or
                        board.grid[self.nx4][self.ny4] == 3 or \
                        board.grid[self.nx4][self.ny4] == 4 or board.grid[self.nx4][self.ny4] == 5 or
                        board.grid[self.nx4][self.ny4] == 6 or \
                        board.grid[self.nx4][self.ny4] == 7 or board.grid[self.nx4][self.ny4] == 8 or
                        board.grid[self.nx4][self.ny4] == 9 or \
                        board.grid[self.nx4][self.ny4] == 10 or board.grid[self.nx4][self.ny4] == 11 or
                        board.grid[self.nx4][self.ny4] == 12) \
                            and (board.grid[self.nx4 - 1][self.ny4 + 1] == "_") and self.D == False:
                        self.killx4 = self.nx4
                        self.killy4 = self.ny4
                        self.nx4 = self.nx4 - 1
                        self.ny4 = self.ny4 + 1
                        if pannel.on:
                            self.optionD = pannel.c.create_oval((self.ny4 * 50 * board.size) + 5 * board.size,
                                                                (self.nx4 * 50 * board.size) + 5 * board.size, ((
                                                                                                                        self.ny4 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx4 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)
                        self.Dd = True
                        self.D = True
                        board.selecting = True
                        board.c_selecting = self.num

        if self.colour == "white":
            if (self.nx1 - 1) > -1 and (self.ny1 - 1) > -1 and self.nx1 > -1 and self.ny1 > -1:
                if (board.grid[self.nx1][self.ny1] == 13 or board.grid[self.nx1][self.ny1] == 14 or
                    board.grid[self.nx1][self.ny1] == 15 or \
                    board.grid[self.nx1][self.ny1] == 16 or board.grid[self.nx1][self.ny1] == 17 or
                    board.grid[self.nx1][self.ny1] == 18 or \
                    board.grid[self.nx1][self.ny1] == 19 or board.grid[self.nx1][self.ny1] == 20 or
                    board.grid[self.nx1][self.ny1] == 21 or \
                    board.grid[self.nx1][self.ny1] == 22 or board.grid[self.nx1][self.ny1] == 23 or
                    board.grid[self.nx1][self.ny1] == 24) \
                        and (board.grid[self.nx1 - 1][self.ny1 - 1] == "_") and self.A == False:
                    self.killx1 = self.nx1
                    self.killy1 = self.ny1
                    self.nx1 = self.nx1 - 1
                    self.ny1 = self.ny1 - 1
                    if pannel.on:
                        self.optionA = pannel.c.create_oval((self.ny1 * 50 * board.size) + 5 * board.size,
                                                            (self.nx1 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny1 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx1 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.A = True
                    self.Ad = True
                    board.selecting = True
                    board.c_selecting = self.num
            if (self.nx2 - 1) > -1 and (self.ny2 + 1) < 8 and self.ny2 > -1 and self.ny2 < 8:
                if (board.grid[self.nx2][self.ny2] == 13 or board.grid[self.nx2][self.ny2] == 14 or
                    board.grid[self.nx2][self.ny2] == 15 or \
                    board.grid[self.nx2][self.ny2] == 16 or board.grid[self.nx2][self.ny2] == 17 or
                    board.grid[self.nx2][self.ny2] == 18 or \
                    board.grid[self.nx2][self.ny2] == 19 or board.grid[self.nx2][self.ny2] == 20 or
                    board.grid[self.nx2][self.ny2] == 21 or \
                    board.grid[self.nx2][self.ny2] == 22 or board.grid[self.nx2][self.ny2] == 23 or
                    board.grid[self.nx2][self.ny2] == 24) \
                        and (board.grid[self.nx2 - 1][self.ny2 + 1] == "_") and self.B == False:
                    self.killx2 = self.nx2
                    self.killy2 = self.ny2
                    self.nx2 = self.nx2 - 1
                    self.ny2 = self.ny2 + 1
                    if pannel.on:
                        self.optionB = pannel.c.create_oval((self.ny2 * 50 * board.size) + 5 * board.size,
                                                            (self.nx2 * 50 * board.size) + 5 * board.size,
                                                            ((
                                                                     self.ny2 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                            ((
                                                                     self.nx2 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                            , outline="blue", width=1 * board.size)
                    self.Bd = True
                    self.B = True
                    board.selecting = True
                    board.c_selecting = self.num
            if self.double:

                if (self.nx3 + 1) < 8 and (self.ny3 - 1) > -1 and self.nx3 < 8 and self.ny3 > -1:
                    if (board.grid[self.nx3][self.ny3] == 13 or board.grid[self.nx3][self.ny3] == 14 or
                        board.grid[self.nx3][self.ny3] == 15 or
                        board.grid[self.nx3][self.ny3] == 16 or board.grid[self.nx3][self.ny3] == 17 or
                        board.grid[self.nx3][self.ny3] == 18 or
                        board.grid[self.nx3][self.ny3] == 19 or board.grid[self.nx3][self.ny3] == 20 or
                        board.grid[self.nx3][self.ny3] == 21 or
                        board.grid[self.nx3][self.ny3] == 22 or board.grid[self.nx3][self.ny3] == 23 or
                        board.grid[self.nx3][self.ny3] == 24) \
                            and (board.grid[self.nx3 + 1][self.ny3 - 1] == "_") and self.C == False:
                        self.killx3 = self.nx3
                        self.killy3 = self.ny3
                        self.nx3 = self.nx3 + 1
                        self.ny3 = self.ny3 - 1
                        if pannel.on:
                            self.optionC = pannel.c.create_oval((self.ny3 * 50 * board.size) + (5 * board.size),
                                                                (self.nx3 * 50 * board.size) + 5 * board.size, ((
                                                                                                                        self.ny3 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx3 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)

                        self.C = True
                        self.Cd = True
                        board.selecting = True
                        board.c_selecting = self.num
                if (self.nx4 + 1) < 8 and (self.ny4 + 1) < 8 and self.nx4 < 8 and self.ny4 < 8:
                    if (board.grid[self.nx4][self.ny4] == 13 or board.grid[self.nx4][self.ny4] == 14 or
                        board.grid[self.nx4][self.ny4] == 15 or
                        board.grid[self.nx4][self.ny4] == 16 or board.grid[self.nx4][self.ny4] == 17 or
                        board.grid[self.nx4][self.ny4] == 18 or
                        board.grid[self.nx4][self.ny4] == 19 or board.grid[self.nx4][self.ny4] == 20 or
                        board.grid[self.nx4][self.ny4] == 21 or
                        board.grid[self.nx4][self.ny4] == 22 or board.grid[self.nx4][self.ny4] == 23 or
                        board.grid[self.nx4][self.ny4] == 24) \
                            and (board.grid[self.nx4 + 1][self.ny4 + 1] == "_") and self.D == False:
                        self.killx4 = self.nx4
                        self.killy4 = self.ny4
                        self.nx4 = self.nx4 + 1
                        self.ny4 = self.ny4 + 1
                        if pannel.on:
                            self.optionD = pannel.c.create_oval((self.ny4 * 50 * board.size) + (5 * board.size),
                                                                (self.nx4 * 50 * board.size) + 5 * board.size, ((
                                                                                                                        self.ny4 * 50 * board.size) + 50 * board.size) - 5 * board.size,
                                                                ((
                                                                         self.nx4 * 50 * board.size) + 50 * board.size) - 5 * board.size
                                                                , outline="blue", width=1 * board.size)

                        self.Dd = True
                        self.D = True
                        board.selecting = True
                        board.c_selecting = self.num

    def checkagain(self):
        if pannel.on:
            board.guidelines(True)
        pannel.c.itemconfigure(self.oval, outline="green", width=3 * board.size)
        if self.colour == "white":
            self.nx1 = (self.x - 1)
            self.nx2 = (self.x - 1)
            self.ny1 = (self.y - 1)
            self.ny2 = (self.y + 1)
            self.nx3 = (self.x + 1)
            self.nx4 = (self.x + 1)
            self.ny3 = (self.y - 1)
            self.ny4 = (self.y + 1)

        if self.colour == "black":
            self.nx1 = (self.x + 1)
            self.nx2 = (self.x + 1)
            self.ny1 = (self.y - 1)
            self.ny2 = (self.y + 1)
            self.nx3 = (self.x - 1)
            self.nx4 = (self.x - 1)
            self.ny3 = (self.y - 1)
            self.ny4 = (self.y + 1)

        self.Ad = False
        self.Bd = False
        self.Cd = False
        self.Dd = False
        self.A = False
        self.B = False
        self.C = False
        self.D = False

        self.checkdouble()

        if self.A is False and self.B is False and self.C is False and self.D is False:
            pannel.c.itemconfigure(self.oval, outline="black", width=1 * board.size)
            board.swapturn()
            pannel.c.update()
            if board.mode == 1:
                Ai.aiturn()
            board.triplejumping = False
        else:
            board.triplejumping = True

    def move(self, across, down):

        board.selecting = False
        moved = False
        jumped = False
        if self.colour == "white":

            if across == self.ny1 and down == self.nx1 and self.A:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx1][self.ny1] = self.num

                self.x = self.nx1
                self.y = self.ny1
                if self.Ad:
                    pannel.c.move(self.oval, -100 * board.size, -100 * board.size)
                    board.kill("A", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, -50 * board.size, -50 * board.size)
                moved = True

            elif across == self.ny2 and down == self.nx2 and self.B:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx2][self.ny2] = self.num
                self.x = self.nx2
                self.y = self.ny2
                if self.Bd:
                    pannel.c.move(self.oval, 100 * board.size, -100 * board.size)
                    board.kill("B", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, 50 * board.size, -50 * board.size)

                moved = True

            elif across == self.ny3 and down == self.nx3 and self.C:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx3][self.ny3] = self.num

                self.x = self.nx3
                self.y = self.ny3
                if self.Cd:
                    pannel.c.move(self.oval, -100 * board.size, 100 * board.size)
                    board.kill("C", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, -50 * board.size, 50 * board.size)
                moved = True

            elif across == self.ny4 and down == self.nx4 and self.D:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx4][self.ny4] = self.num

                self.x = self.nx4
                self.y = self.ny4
                if self.Dd:
                    pannel.c.move(self.oval, 100 * board.size, 100 * board.size)
                    board.kill("D", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, 50 * board.size, 50 * board.size)
                moved = True

            if moved:
                if self.x == 0 and self.double == False:
                    self.double = True
                    pannel.c.itemconfigure(self.oval, fill="#FC9797")
                    if board.triplejumping:
                        board.swapturn()
                    jumped = False

        elif self.colour == "black":

            if across == self.ny1 and down == self.nx1 and self.A:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx1][self.ny1] = self.num

                self.x = self.nx1
                self.y = self.ny1
                if self.Ad:
                    pannel.c.move(self.oval, -100 * board.size, 100 * board.size)
                    board.kill("A", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, -50 * board.size, 50 * board.size)

                moved = True

            elif across == self.ny2 and down == self.nx2 and self.B:
                board.grid[self.x][self.y] = "_"

                board.grid[self.nx2][self.ny2] = self.num
                self.x = self.nx2
                self.y = self.ny2
                if self.Bd:
                    pannel.c.move(self.oval, 100 * board.size, 100 * board.size)
                    board.kill("B", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, 50 * board.size, 50 * board.size)

                moved = True

            elif across == self.ny3 and down == self.nx3 and self.C:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx3][self.ny3] = self.num

                self.x = self.nx3
                self.y = self.ny3
                if self.Cd:
                    pannel.c.move(self.oval, -100 * board.size, -100 * board.size)
                    board.kill("C", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True
                else:
                    pannel.c.move(self.oval, -50 * board.size, -50 * board.size)
                moved = True

            elif across == self.ny4 and down == self.nx4 and self.D:

                board.grid[self.x][self.y] = "_"

                board.grid[self.nx4][self.ny4] = self.num

                self.x = self.nx4
                self.y = self.ny4
                if self.Dd:
                    pannel.c.move(self.oval, 100 * board.size, -100 * board.size)
                    board.kill("D", self.killx1, self.killx2, self.killy1, self.killy2, self.killx3, self.killx4,
                               self.killy3, self.killy4)
                    jumped = True

                else:
                    pannel.c.move(self.oval, 50 * board.size, -50 * board.size)
                moved = True

            if moved:
                if self.x == 7 and self.double == False:
                    self.double = True
                    pannel.c.itemconfigure(self.oval, fill="#810606")
                    if board.triplejumping:
                        board.swapturn()
                    jumped = False

        if pannel.on:
            if self.A:
                pannel.c.delete(self.optionA)
            if self.B:
                pannel.c.delete(self.optionB)
            if self.C:
                pannel.c.delete(self.optionC)
            if self.D:
                pannel.c.delete(self.optionD)
        if self.A:
            self.A = False

        if self.B:
            self.B = False

        if self.C:
            self.C = False

        if self.D:
            self.D = False
        if not pannel.Aion:
            board.showounternums(False)
            board.showounternums(True)
        board.count()
        if jumped:
            self.checkagain()
        else:
            pannel.c.itemconfigure(self.oval, outline="black", width=1 * board.size)
            if moved:
                board.swapturn()
                pannel.c.update()
                if board.mode == 1:
                    Ai.aiturn()
                pannel.c.update()
        board.checkfordraw()
        if pannel.on:
            board.guidelines(False)

    def aimove(self, command):
        newgrid1 = copy.deepcopy(board.grid)
        # print(self.x, self.y)

        if not command[2]:
            if command[1] == "NE":
                self.x = self.x - 1
                self.y = self.y + 1
                pannel.c.move(self.oval, 50 * board.size, -50 * board.size)
            elif command[1] == "SE":
                self.x = self.x + 1
                self.y = self.y + 1
                pannel.c.move(self.oval, 50 * board.size, 50 * board.size)
            elif command[1] == "SW":
                self.x = self.x + 1
                self.y = self.y - 1
                pannel.c.move(self.oval, -50 * board.size, 50 * board.size)
            elif command[1] == "NW":
                self.x = self.x - 1
                self.y = self.y - 1
                pannel.c.move(self.oval, -50 * board.size, -50 * board.size)
        else:
            if command[1] == "NE":
                board.kill("A", self.x - 1, 0, self.y + 1, 0, 0, 0, 0, 0)
                self.x = self.x - 2
                self.y = self.y + 2
                pannel.c.move(self.oval, 100 * board.size, -100 * board.size)
            elif command[1] == "SE":
                board.kill("A", self.x + 1, 0, self.y + 1, 0, 0, 0, 0, 0)
                self.x = self.x + 2
                self.y = self.y + 2
                pannel.c.move(self.oval, 100 * board.size, 100 * board.size)
            elif command[1] == "SW":
                board.kill("A", self.x + 1, 0, self.y - 1, 0, 0, 0, 0, 0)
                self.x = self.x + 2
                self.y = self.y - 2
                pannel.c.move(self.oval, -100 * board.size, 100 * board.size)
            elif command[1] == "NW":
                board.kill("A", self.x - 1, 0, self.y - 1, 0, 0, 0, 0, 0)
                self.x = self.x - 2
                self.y = self.y - 2
                pannel.c.move(self.oval, -100 * board.size, -100 * board.size)
        newgrid = Ai.createnewgrid(newgrid1, command[1], command[0], command[2])
        board.grid *= 0
        board.grid = copy.deepcopy(newgrid)
        pannel.c.after(500, board.swapturn())
        if self.x == 7 and self.double is False:
            self.double = True
            pannel.c.itemconfigure(self.oval, fill="#810606")
        if not pannel.Aion:
            board.showounternums(False)
            board.showounternums(True)
        board.count()
        board.checkfordraw()

    def createguideline(self):
        if pannel.on:
            if self.num in board.inplay:
                pannel.c.itemconfigure(self.oval, outline="blue", width=2 * board.size)
            else:
                self.changeback()
        else:
            self.changeback()


class Ai:


    def createstep(self, move, grid1):
        grid2 = self.createnewgrid(grid1, move[1], move[0], move[2])
        score = self.getscore(grid2)
        comp = self.gridcompress(grid2)
        step = [move, comp, score]
        return step, grid2

    def createposibilities(self, grid, turn):
        moveableblack, moveablewhite = self.countmoveablecounters(grid)
        if turn == "w":
            moveables = moveablewhite
        else:
            moveables = moveableblack
        posibilities = self.checkmoveablelocations(grid, moveables)
        return posibilities

    def aiturn(self):

        allmoves = []
        posibilities = self.createposibilities(board.grid, "b")
        for i in range(len(posibilities)):
            step1, grid1 = self.createstep(posibilities[i], board.grid)

            posibilities2 = self.createposibilities(grid1, "w")
            for i2 in range(len(posibilities2)):
                step2, grid2 = self.createstep(posibilities2[i2], grid1)
                posibilities3 = self.createposibilities(grid2, "b")
                for i3 in range(len(posibilities3)):
                    step3, grid3 = self.createstep(posibilities3[i3], grid2)
                    posibilities4 = self.createposibilities(grid3, "w")
                    for i4 in range(len(posibilities4)):
                        step4, grid4 = self.createstep(posibilities4[i4], grid3)
                        posibilities5 = self.createposibilities(grid4, "b")
                        for i5 in range(len(posibilities5)):
                            step5, grid5 = self.createstep(posibilities5[i5], grid4)
                            move = [step1,step2,step3,step4,step5]
                            allmoves.append(move)
        print(len(allmoves))
        probabalmoves = self.keepmin(posibilities,0,allmoves)
        if probabalmoves != []:
            a = probabalmoves[0][2][0]
            b = [a]

            for i in range(len(probabalmoves)):
                if probabalmoves[i][2][0] != a:
                    a = probabalmoves[i][2][0]
                    b.append(probabalmoves[i][2][0])
            probabalmoves2 = self.keepmin(b, 2, probabalmoves)
            a = probabalmoves2[0][4][2]
            b *= 0




            for i in range(len(probabalmoves2)):


                if probabalmoves2[i][4][2] > a:
                    b *= 0
                    b.append(probabalmoves2[i])
                    a = probabalmoves2[i][4][2]
                elif probabalmoves2[i][4][2] == a:
                    b.append(probabalmoves2[i])
            finalposibilities = []
            for i in range(len(b)):
                finalposibilities.append(b[i][0][0])
            finalposibilitiesmodes = []
            for i in range(len(finalposibilities)):
                b = 0
                for i2 in range(len(finalposibilities)):
                    if finalposibilities[i] == finalposibilities[i2]:
                        b = b + 1
                finalposibilitiesmodes.append(b)
            a = 0
            move = []
            for i in range(len(finalposibilitiesmodes)):
                if i > a:
                    a = i
            move = finalposibilities[a]
        else:
            moveableblack, moveablewhite = self.countmoveablecounters(board.grid)
            posibilities = self.checkmoveablelocations(board.grid, moveableblack)
            if len(posibilities) == 0:
                board.checkfordraw()
            move = posibilities[0]
        self.sendmove(move)
    def keepmin(self,posibilities,b,allmoves):
        probabalmoves = []
        for i in range(len(posibilities)):
            a = []
            a *= 0
            for i2 in range(len(allmoves)):
                if allmoves[i2][b][0] == posibilities[i]:
                    a.append(allmoves[i2])
            lowestmoves = self.removeImprobbablemoves(a)
            for i2 in range(len(lowestmoves)):
                probabalmoves.append(lowestmoves[i2])
            #probabalmoves.append(lowestmoves)
        return probabalmoves
    # def getMax(self,final,grid):
    def removeImprobbablemoves(self,moves):
        lowest = moves[0][1][2]
        lowestmoves = []

        for i in range(len(moves)):
            if moves[i][1][2] < lowest:
                lowest = moves[i][1][2]
                lowestmoves *= 0
                lowestmoves.append(moves[i])
            elif moves[i][1][2] == lowest:
                lowestmoves.append(moves[i])
        return lowestmoves
    def convertToLetter(self, input):
        index = [
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x"],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]]
        input -= 1

        return index[0][input]

    def gridcompress(self, inputa):
        #inputb = copy.deepcopy(inputa)
#
 #       for x in range(0, 8):
  #          for y in range(0, 8):
   #             if inputb[x][y] != "_":
    #                letter = self.convertToLetter(inputb[x][y])
     #           else:
      #              letter = "_"
       #         inputb[x][y] = letter
        #output = f"{inputb[0][1]}{inputb[0][3]}{inputb[0][5]}{inputb[0][7]}{inputb[1][0]}{inputb[1][2]}{inputb[1][4]}" \
         #   f"{inputb[1][6]}{inputb[2][1]}" \
          #  f"{inputb[2][3]}{inputb[2][5]}{inputb[2][7]}{inputb[3][0]}{inputb[3][2]}{inputb[3][4]}{inputb[3][6]}" \
           # f"{inputb[4][1]}{inputb[4][3]}{inputb[4][5]}" \
            #f"{inputb[4][7]}{inputb[5][0]}{inputb[5][2]}{inputb[5][4]}{inputb[5][6]}{inputb[6][1]}{inputb[6][3]}" \
            #f"{inputb[6][5]}{inputb[6][7]}" \
            #f"{inputb[7][0]}{inputb[7][2]}{inputb[7][4]}{inputb[7][6]}"
        return ""

    def aiturn_(self):

        moveableblack, moveablewhite = self.countmoveablecounters(board.grid)

        posibilities = self.checkmoveablelocations(board.grid, moveableblack)

        grids = []

        for i in range(len(posibilities)):
            grid = self.createnewgrid(board.grid, posibilities[i][1], posibilities[i][0], posibilities[i][2])
            grids.append(grid)
            score = self.getscore(grid)
            if score == 1000:
                self.sendmove(posibilities[i])
        secondgrids = []
        for i in range(len(grids)):
            moveableblack, moveablewhite = self.countmoveablecounters(grids[i])
            posibilities2 = self.checkmoveablelocations(grids[i], moveablewhite)
            secondgrid = []
            secondgrid *= 0
            secondgridscores = []
            secondgridscores *= 0
            for i2 in range(len(posibilities2)):
                grid = self.createnewgrid(grids[i], posibilities2[i2][1], posibilities2[i2][0],
                                          posibilities2[i2][2])
                secondgrid.append(grid)
                score = self.getscore(grid)

                secondgridscores.append(score)

            highestscore = 10000
            highestscores = []
            highestscores *= 0
            for i2 in range(len(secondgridscores)):
                if secondgridscores[i2] < highestscore:
                    highestscore = secondgridscores[i2]
                    highestscores *= 0
                    highestscores.append(i2)
                elif secondgridscores[i2] == highestscore:
                    highestscores.append(i2)
            a = len(secondgrid)

            for i2 in range(len(secondgrid)):
                a = a - 1

                if secondgridscores[i2] != highestscore:
                    secondgrid.pop(a)

            secondgrids.append(secondgrid)

        thirdgrids = []

        for i in range(len(secondgrids)):
            thirdgrids2 = []
            thirdgrids2 *= 0
            for i2 in range(len(secondgrids[i])):
                moveableblack, moveablewhite = self.countmoveablecounters(secondgrids[i][i2])
                posibilities2 = self.checkmoveablelocations(secondgrids[i][i2], moveableblack)
                thirdgrid = []
                thirdgrid *= 0
                thirdgridscores = []
                thirdgridscores *= 0
                for i3 in range(len(posibilities2)):
                    grid = self.createnewgrid(secondgrids[i][i2], posibilities2[i3][1], posibilities2[i3][0],
                                              posibilities2[i3][2])
                    thirdgrid.append(grid)
                    score = self.getscore(grid)
                    thirdgridscores.append(score)

                thirdgrids2.append(thirdgrid)
            thirdgrids.append(thirdgrids2)

        cel = []
        for i in range(len(thirdgrids)):
            cel2 = []
            cel2 *= 0
            for i2 in range(len(thirdgrids[i])):
                cel3 = []
                cel3 *= 0
                for i3 in range(len(thirdgrids[i][i2])):
                    scored = self.getscore(thirdgrids[i][i2][i3])

                    cel3.append(scored)
                cel2.append(cel3)
            cel.append(cel2)

        highestscore = 0

        for i in range(len(thirdgrids)):

            for i2 in range(len(thirdgrids[i])):

                for i3 in range(len(thirdgrids[i][i2])):
                    if cel[i][i2][i3] > highestscore:
                        highestscore = cel[i][i2][i3]

        # print(highestscore)
        bestmoves = []
        for i in range(len(thirdgrids)):

            for i2 in range(len(thirdgrids[i])):

                for i3 in range(len(thirdgrids[i][i2])):
                    if cel[i][i2][i3] == highestscore:
                        bestmoves.append(i)

        # print(bestmoves)
        # print(grids)
        mode = self.findMode(bestmoves)
        if mode == -1:
            mode = random.choice(bestmoves)
        # print(posibilities)
        # print(mode)
        self.sendmove(posibilities[mode])

    def sendmove(self, command):
        counternum = command[0]
        if counternum == 13:
            board.counter13.aimove(command)
        elif counternum == 14:
            board.counter14.aimove(command)

        elif counternum == 15:
            board.counter15.aimove(command)

        elif counternum == 16:
            board.counter16.aimove(command)

        elif counternum == 17:
            board.counter17.aimove(command)

        elif counternum == 18:
            board.counter18.aimove(command)

        elif counternum == 19:
            board.counter19.aimove(command)

        elif counternum == 20:
            board.counter20.aimove(command)

        elif counternum == 21:
            board.counter21.aimove(command)

        elif counternum == 22:
            board.counter22.aimove(command)

        elif counternum == 23:
            board.counter23.aimove(command)

        elif counternum == 24:
            board.counter24.aimove(command)



    def countmoveablecounters(self, locations):
        moveablewhite = []
        moveableblack = []
        # print(f"\n\n\n{locations[0]}\n{locations[1]}\n{locations[2]}\n{locations[3]}\n{locations[4]}\n{locations[5]}\n{locations[6]}\n{locations[7]}\n")
        for x in range(0, 8):
            for y in range(0, 8):
                # print(locations[x][y])
                if locations[x][y] != "_":
                    if (locations[x][y] - 12) <= 0:
                        moveable = self.checkifmoveable(locations, x, y)
                        if moveable:
                            moveablewhite.append(locations[x][y])
                    else:
                        moveable = self.checkifmoveable(locations, x, y)
                        if moveable:
                            moveableblack.append(locations[x][y])
                            # print(locations[x][y],"True")
        return moveableblack, moveablewhite

    def checkifmoveable(self, locations, x, y):

        double, colour = self.getinfo(locations[x][y])
        moveable = False

        if double == True or colour == "white":
            if x > 0 and y > 0:
                if locations[x - 1][y - 1] == "_":
                    moveable = True
                elif x > 1 and y > 1:
                    d, jcolour = self.getinfo(locations[x - 1][y - 1])
                    if colour == "white" and jcolour == "black" and locations[x - 2][y - 2] == "_":
                        moveable = True
                    elif colour == "black" and jcolour == "white" and locations[x - 2][y - 2] == "_":
                        moveable = True
            if x > 0 and y < 7:
                if locations[x - 1][y + 1] == "_":
                    moveable = True
                elif x > 1 and y < 6:
                    d, jcolour = self.getinfo(locations[x - 1][y + 1])
                    if colour == "white" and jcolour == "black" and locations[x - 2][y + 2] == "_":
                        moveable = True
                    elif colour == "black" and jcolour == "white" and locations[x - 2][y + 2] == "_":
                        moveable = True
        if double == True or colour == "black":
            if x < 7 and y > 0:
                if locations[x + 1][y - 1] == "_":
                    moveable = True
                elif x < 6 and y > 0:
                    d, jcolour = self.getinfo(locations[x + 1][y - 1])
                    if colour == "white" and jcolour == "black" and locations[x + 2][y - 2] == "_":
                        moveable = True
                    elif colour == "black" and jcolour == "white" and locations[x + 2][y - 2] == "_":
                        moveable = True
            if x < 7 and y < 7:
                if locations[x + 1][y + 1] == "_":
                    moveable = True
                elif x > 6 and y < 6:
                    d, jcolour = self.getinfo(locations[x + 1][y + 1])
                    if colour == "white" and jcolour == "black" and locations[x + 2][y + 2] == "_":
                        moveable = True
                    elif colour == "black" and jcolour == "white" and locations[x + 2][y + 2] == "_":
                        moveable = True
        # print(f"{locations[x][y]} is {moveable} when x={x} and y={y}")
        return moveable

    def checkmoveablelocations(self, locations, counters):

        posibilities = []
        for i in range(len(counters)):
            for x in range(0, 8):
                for y in range(0, 8):
                    if locations[x][y] == counters[i]:
                        double, colour = self.getinfo(locations[x][y])
                        if double == True or colour == "white":
                            if x > 0 and y > 0:
                                if locations[x - 1][y - 1] == "_":
                                    posibilities.append([locations[x][y], "NW", False])
                                elif x > 1 and y > 1:
                                    d, jcolour = self.getinfo(locations[x - 1][y - 1])
                                    if colour == "white" and jcolour == "black" and locations[x - 2][y - 2] == "_":
                                        posibilities.append([locations[x][y], "NW", True])
                                    elif colour == "black" and jcolour == "white" and locations[x - 2][y - 2] == "_":
                                        posibilities.append([locations[x][y], "NW", True])
                            if x > 0 and y < 7:
                                if locations[x - 1][y + 1] == "_":
                                    posibilities.append([locations[x][y], "NE", False])
                                elif x > 1 and y < 6:
                                    d, jcolour = self.getinfo(locations[x - 1][y + 1])
                                    if colour == "white" and jcolour == "black" and locations[x - 2][y + 2] == "_":
                                        posibilities.append([locations[x][y], "NE", True])
                                    elif colour == "black" and jcolour == "white" and locations[x - 2][y + 2] == "_":
                                        posibilities.append([locations[x][y], "NE", True])
                        if double == True or colour == "black":
                            if x < 7 and y > 0:
                                if locations[x + 1][y - 1] == "_":
                                    posibilities.append([locations[x][y], "SW", False])
                                elif x < 6 and y > 1:
                                    d, jcolour = self.getinfo(locations[x + 1][y - 1])
                                    if colour == "white" and jcolour == "black" and locations[x + 2][y - 2] == "_":
                                        posibilities.append([locations[x][y], "SW", True])
                                    elif colour == "black" and jcolour == "white" and locations[x + 2][y - 2] == "_":
                                        posibilities.append([locations[x][y], "SW", True])
                            if x < 7 and y < 7:
                                if locations[x + 1][y + 1] == "_":
                                    posibilities.append([locations[x][y], "SE", False])
                                elif x < 6 and y < 6:
                                    d, jcolour = self.getinfo(locations[x + 1][y + 1])
                                    if colour == "white" and jcolour == "black" and locations[x + 2][y + 2] == "_":
                                        posibilities.append([locations[x][y], "SE", True])
                                    elif colour == "black" and jcolour == "white" and locations[x + 2][y + 2] == "_":
                                        posibilities.append([locations[x][y], "SE", True])
        return posibilities

    def createnewgrid(self, oldgrid, direction, counter, doublejump):
        newgrid = copy.deepcopy(oldgrid)
        for x in range(0, 8):
            for y in range(0, 8):
                if oldgrid[x][y] == counter:
                    newgrid[x][y] = "_"
                    if direction == "NE":
                        if doublejump == False:
                            newgrid[x - 1][y + 1] = counter
                        else:
                            newgrid[x - 1][y + 1] = "_"
                            newgrid[x - 2][y + 2] = counter
                    elif direction == "SE":
                        if doublejump == False:
                            newgrid[x + 1][y + 1] = counter
                        else:
                            newgrid[x + 1][y + 1] = "_"
                            newgrid[x + 2][y + 2] = counter
                    elif direction == "SW":
                        if doublejump == False:
                            newgrid[x + 1][y - 1] = counter
                        else:
                            newgrid[x + 1][y - 1] = "_"
                            newgrid[x + 2][y - 2] = counter
                    elif direction == "NW":
                        if doublejump == False:
                            newgrid[x - 1][y - 1] = counter
                        else:
                            newgrid[x - 1][y - 1] = "_"
                            newgrid[x - 2][y - 2] = counter
        return (newgrid)

    def getinfo(self, counternum):

        if counternum == 1:
            double = board.counter01.double
            colour = board.counter01.colour
        elif counternum == 2:
            double = board.counter02.double
            colour = board.counter02.colour
        elif counternum == 3:
            double = board.counter03.double
            colour = board.counter03.colour
        elif counternum == 4:
            double = board.counter04.double
            colour = board.counter04.colour
        elif counternum == 5:
            double = board.counter05.double
            colour = board.counter05.colour
        elif counternum == 6:
            double = board.counter06.double
            colour = board.counter06.colour
        elif counternum == 7:
            double = board.counter07.double
            colour = board.counter07.colour
        elif counternum == 8:
            double = board.counter08.double
            colour = board.counter08.colour
        elif counternum == 9:
            double = board.counter09.double
            colour = board.counter09.colour
        elif counternum == 10:
            double = board.counter10.double
            colour = board.counter10.colour
        elif counternum == 11:
            double = board.counter11.double
            colour = board.counter11.colour
        elif counternum == 12:
            double = board.counter12.double
            colour = board.counter12.colour
        elif counternum == 13:
            double = board.counter13.double
            colour = board.counter13.colour
        elif counternum == 14:
            double = board.counter14.double
            colour = board.counter14.colour
        elif counternum == 15:
            double = board.counter15.double
            colour = board.counter15.colour
        elif counternum == 16:
            double = board.counter16.double
            colour = board.counter16.colour
        elif counternum == 17:
            double = board.counter17.double
            colour = board.counter17.colour
        elif counternum == 18:
            double = board.counter18.double
            colour = board.counter18.colour
        elif counternum == 19:
            double = board.counter19.double
            colour = board.counter19.colour
        elif counternum == 20:
            double = board.counter20.double
            colour = board.counter20.colour
        elif counternum == 21:
            double = board.counter21.double
            colour = board.counter21.colour
        elif counternum == 22:
            double = board.counter22.double
            colour = board.counter22.colour
        elif counternum == 23:
            double = board.counter23.double
            colour = board.counter23.colour
        elif counternum == 24:
            double = board.counter24.double
            colour = board.counter24.colour
        return double, colour

    def getscore(self, grid):

        WhiteCounters = 0
        BlackCounters = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if grid[y][x] != "_":
                    temp = grid[y][x] - 12
                    if temp <= 0:
                        WhiteCounters = WhiteCounters + 1

                    else:
                        BlackCounters = BlackCounters + 1

        score = BlackCounters - WhiteCounters
        for i in range(1, 13):
            double, colour = self.getinfo(i)
            if double:
                score = score - 1
        for i in range(12, 25):
            double, colour = self.getinfo(i)
            if double:
                score = score + 1
        # print(score)
        if WhiteCounters == 0:
            score = 1000
        if BlackCounters == 0:
            score = -1000
        return score


class Buttons:

    def run(self):
        self.pannel = Frame(width=400 * board.size, height=100 * board.size, bg="light blue")
        self.pannel.pack(fill="x", padx=50, pady=10)
        self.scored = Frame(self.pannel, bg="light blue")
        self.scored.pack(pady=10 * board.size, fill="x")
        self.buttons = Frame(self.pannel, bg="light blue")

        self.whitesLabel = Label(self.scored, bg="light blue", font=("Verdana", int(13 * board.size)))
        self.whitesLabel.pack(side="left")
        self.blacksLabel = Label(self.scored, bg="light blue", font=("Verdana", int(13 * board.size)))
        self.blacksLabel.pack(side="right")
        self.c = Canvas(self.pannel, height=400 * board.size, width=400 * board.size, highlightbackground="black",
                        highlightthickness=1)
        self.c.pack()
        self.buttons.pack(pady=10 * board.size)

        self.on = False
        self.guides = Button(self.buttons, text="Guidelines are off", command=self.toggle,
                             activebackground="light blue", width=int(13 + board.size),
                             font=("Verdana", int(15 * board.size)))
        self.guides.grid(column="0", row="0")
        Label(self.buttons, text="", width=int(2 * board.size), bg="light blue").grid(column="1", row="0")
        self.reset = Button(self.buttons, text="Restart", width=int(13 + board.size), command=board.repbutton,
                            font=("Verdana", int(15 * board.size)))
        self.reset.grid(column="2", row="0")
        Label(self.buttons, text="", width=int(2 * board.size), bg="light blue").grid(column="3", row="0")
        self.Aion = True
        self.AiButton = Button(self.buttons, text="Numbers Off", command=self.toggleAi,
                               activebackground="light blue", width=int(13 + board.size),
                               font=("Verdana", int(15 * board.size)))
        self.AiButton.grid(column="4", row="0")
        self.MenuButton = Button(self.buttons, text="Menu", width=int(13 + board.size), command=menu.openmenu,
                                 font=("Verdana", int(15 * board.size)))
        Label(self.buttons, text="", bg="light blue").grid(column="2", row="1")
        self.MenuButton.grid(column="2", row="2")

    def toggle(self):

        if self.on is False:
            self.guides.configure(text="Guidelines are on", relief=SUNKEN, font=("Verdana", int(15 * board.size)))

            self.on = True
            board.guidelines(False)
        else:
            self.guides.configure(text="Guidelines are off", relief=RAISED, font=("Verdana", int(15 * board.size)))
            self.on = False
            board.guidelines(False)
        # Ai.aiturn()

    def toggleAi(self):
        if self.Aion is False:
            self.AiButton.configure(text="Numbers off", relief=SUNKEN, font=("Verdana", int(15 * board.size)))

            self.Aion = True
            board.showounternums(False)

        else:
            self.AiButton.configure(text="Numbers on", relief=RAISED, font=("Verdana", int(15 * board.size)))
            self.Aion = False
            board.showounternums(True)


class DebugWindow:
    def __init__(self):
        self.debug = Toplevel(root)
        Button(self.debug, text="swap turns", command=board.swapturn).pack()


board = GameBoard(1.25)

pannel = Buttons()

menu = MenuScreen()

root.config(bg="light blue")
root.title("Drafts")
#root.iconbitmap(r'checker-board.ico')
Ai = Ai()

mainloop()
