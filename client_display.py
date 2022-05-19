import tkinter as tk
import socket

LARGE_FONT_STYLE = ("Arial", 40,"bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFUALT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
LIGHT_GRAY = "#F5F5F5"
LIGHT_BLUE = "#CCEDFF"
LABEL_COLOR = "#25265E"

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


class Display:
	def __init__(self):
		self.window = tk.Tk()
		self.window.geometry("375x667") #Size for start
		self.window.resizable(0,0) #Size_resizeable
		self.window.title("Test") #Title Tag in top

		self.total_expression = ""
		self.current_expression = ""

		self.display_frame = self.create_display_frame()
		
		self.total_label, self.label = self.create_display_labels()

		self.digits = {
			int(number_list[0]): (1, 1), int(number_list[1]): (1, 2), int(number_list[2]): (1, 3), int(number_list[3]): (1, 4)
		}

		self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
		self.buttons_frame = self.create_buttons_frame()
		
		self.buttons_frame.rowconfigure(0, weight=1)
		for x in range(1,5):
			self.buttons_frame.rowconfigure(x, weight=1)
			self.buttons_frame.columnconfigure(x, weight=1)

		self.create_digit_buttons()
		self.create_operator_button()
		self.create_special_button()

	def create_special_button(self):
		self.create_clear_button()
		self.create_equals_button()

	def create_display_labels(self):
		total_label = tk.Label(self.display_frame, text=self.total_expression,
		 anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)#CENTER ทดไว้แก้
		total_label.pack(expand=True, fill='both')

		label = tk.Label(self.display_frame, text=self.current_expression,
		 anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)#CENTER ทดไว้แก้
		label.pack(expand=True, fill='both')

		return total_label, label
		
	def create_display_frame(self):
		frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
		frame.pack(expand=True, fill='both')
		return frame

	def add_to_expression(self, value):
		print(self)
		self.current_expression += str(value)
		self.update_label()

	def create_digit_buttons(self):
		for digit, grid_value in self.digits.items():
			if(grid_value[1] == 1):
				button_1 = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF",
				fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x = digit: [self.add_to_expression(x),button_1.pack_forget()])
				button_1.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
			if(grid_value[1] == 2):
				button_2 = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF",
				fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x = digit: [self.add_to_expression(x),button_2.pack_forget()])
				button_2.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
			if(grid_value[1] == 3):
				button_3 = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF",
				fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x = digit: [self.add_to_expression(x),button_3.pack_forget()])
				button_3.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
			if(grid_value[1] == 4):
				button_4 = tk.Button(self.buttons_frame, text=str(digit), bg="#FFFFFF",
				fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x = digit: [self.add_to_expression(x),button_4.pack_forget()])
				button_4.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

	def append_operator(self, operator):
		print("operator")
		self.current_expression += operator
		self.total_expression += self.current_expression
		self.current_expression = ""
		self.update_total_label()
		self.update_label()

	def create_operator_button(self):
		i=1
		for operator , symbol in self.operations.items():
			button = tk.Button(self.buttons_frame, text=symbol,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFUALT_FONT_STYLE,borderwidth=0, command=lambda x=operator: self.append_operator(x))
			button.grid(row=2,column=i,sticky=tk.NSEW)
			i+=1

	def clear(self):
		self.current_expression = ""
		self.total_expression = ""
		self.update_label()
		self.update_total_label()

	def create_clear_button(self):
		button = tk.Button(self.buttons_frame, text="C",bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFUALT_FONT_STYLE,borderwidth=0, command=self.clear)
		button.grid(row=4,column=1,columnspan=2,sticky=tk.NSEW)

	def evaluate(self):
		self.total_expression += self.current_expression
		self.update_total_label()

		self.current_expression = str(eval(self.total_expression))

		self.total_expression = ""
		self.update_label()

	def create_buttons_frame(self):
		frame = tk.Frame(self.window)
		frame.pack(expand=True, fill='both')
		return frame

	def create_equals_button(self):
		button = tk.Button(self.buttons_frame, text="=",bg=LIGHT_BLUE,fg=LABEL_COLOR,font=DEFUALT_FONT_STYLE,borderwidth=0,command=self.evaluate)
		button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
		
	def update_total_label(self):
		expression = self.total_expression
		for operator, symbol in self.operations.items():
			expression = expression.replace(operator, f' {symbol} ')
		self.total_label.config(text=expression)

	def update_label(self):
		self.label.config(text = self.current_expression)

	def run(self):
		self.window.mainloop()

if __name__ == "__main__":
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
		client.connect((HOST, PORT))
		number_list = []
		for i in range(4):
			number_rev = client.recv(1024).decode()
			number_list.append(number_rev)
		client_display = Display()
		client_display.run()