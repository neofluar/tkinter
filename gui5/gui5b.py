from gui5.gui5a import HelloButton


class MyButton(HelloButton):
    def callback(self):
        print('Go and f* yourself!')


if __name__ == '__main__':
    MyButton(None, text='PRESS ME :)').mainloop()
