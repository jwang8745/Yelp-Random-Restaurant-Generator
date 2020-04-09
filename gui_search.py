import tkinter
import randomizer_parts


class EmptyFieldsError(Exception):
    pass

class yelp_randomizer_search:
    def __init__(self):

        DEFAULT_FONT = ('Helvetica', 20)

        self._root_window = tkinter.Tk()

        ###TITLE####
        self._title = tkinter.Label(master = self._root_window,
                                            text = 'Yelp Randomizer',
                                            font = ('Helvetica', 25))
        self._title.grid(row = 0, column = 1,
                                 padx = 10, pady = 10,
                                 sticky = tkinter.W + tkinter.N + tkinter.E)

        ## Ask for Type of Restaurant
        self._find = tkinter.Label(master = self._root_window,
                                   text = 'Find: ',
                                   font = DEFAULT_FONT)
        
        self._find.grid(row = 1, column = 0)

        self._find_input = tkinter.Entry(master = self._root_window,
                                            width = 20,
                                            font = DEFAULT_FONT)
        
        self._find_input.grid(row = 1, column = 1,
                                 padx = 10, pady = 10,
                                 sticky = tkinter.E + tkinter.N + tkinter.W)
        

        self._find_instructions = tkinter.Label(master = self._root_window,
                                                   text = 'Ex: (Food, Chinese, Mexican, American, Fast Food)',
                                                   font = DEFAULT_FONT)
        self._find_instructions.grid(row = 1, column = 2,
                                        padx = 10, pady = 10,
                                        sticky = tkinter.W + tkinter.N + tkinter.E)

        ##ASK FOR LOCATION
        
        self._location = tkinter.Label(master = self._root_window,
                                   text = 'Near: ',
                                   font = DEFAULT_FONT)
        
        self._location.grid(row = 2, column = 0)

        self._location_input = tkinter.Entry(master = self._root_window,
                                            width = 20,
                                            font = DEFAULT_FONT)
        
        self._location_input.grid(row = 2, column = 1,
                                 padx = 10, pady = 10,
                                 sticky = tkinter.E + tkinter.N + tkinter.W)

        self._location_instructions = tkinter.Label(master = self._root_window,
                                                   text = 'Ex: (92154, Chula Vista, San Diego)',
                                                   font = DEFAULT_FONT)
        self._location_instructions.grid(row = 2, column = 2,
                                        padx = 10, pady = 10,
                                        sticky = tkinter.W + tkinter.N + tkinter.E)

        ## ASK PRICE RANGE
        self._price = tkinter.Label(master = self._root_window,
                                   text = 'Price Range: ',
                                   font = DEFAULT_FONT)
        
        self._price.grid(row = 3, column = 0)
        
        self._price_frame = tkinter.Frame(self._root_window)
        self._price_frame.grid(row = 3, column = 1)

        ##Price range of 1
        self.price_1 = tkinter.StringVar()
        self._price_1 = tkinter.Checkbutton(master = self._price_frame,
                                            text = "$", onvalue = '1', offvalue = '',
                                            variable = self.price_1,
                                            font = ('helvetica', 15))
        self._price_1.grid(row = 0, column = 0)
        
        self._price_1.select()
        self._price_1.var = self.price_1



        
        ##Price range of 2
        self.price_2 = tkinter.StringVar()
        self._price_2 = tkinter.Checkbutton(master = self._price_frame,
                                            text = "$$",onvalue = '2', offvalue = '',
                                            variable = self.price_2,
                                            font = ('helvetica', 15))
        self._price_2.grid(row = 1, column = 0)

        
        ##PRICE RANGE OF 3
        self.price_3 = tkinter.StringVar()
        self._price_3 = tkinter.Checkbutton(master = self._price_frame,
                                            text = "$$$", onvalue = '3', offvalue = '',
                                            variable = self.price_3,
                                            font = ('helvetica', 15))
        self._price_3.grid(row = 2, column = 0)

        self.price_4 = tkinter.StringVar()
        self._price_4 = tkinter.Checkbutton(master = self._price_frame,
                                            text = "$$$$",onvalue = '4', offvalue = '',
                                            variable = self.price_4,
                                            font = ('helvetica', 15))
        self._price_4.grid(row = 3, column = 0)
        
        self._price_2.select()
        self._price_3.select()
        self._price_4.select()

        self._price_info = tkinter.Label(master = self._root_window,
                                   text = '$= under $10. $$=11-30. $$$=31-60. $$$$= over $61',
                                   font = DEFAULT_FONT)
        
        self._price_info.grid(row = 3, column = 2)

        ## Ask if OPEN NOW?

        ##Variable to store if yes or now
        self.open_var = "True"

        self._open = tkinter.Label(master = self._root_window,
                                   text = 'Open Now: ',
                                   font = DEFAULT_FONT)
        
        self._open.grid(row = 4, column = 0)

        self._open_frame = tkinter.Frame(self._root_window)
        self._open_frame.grid(row = 4, column = 1, sticky = tkinter.W + tkinter.N + tkinter.E+ tkinter.S)

        self._open_yes = tkinter.Radiobutton(master = self._open_frame,
                                   text = 'Yes', variable = self.open_var, value = "True",
                                             command = self.set_open_true,
                                   font = ('helvetica', 15))
        
        self._open_yes.pack()

        self._open_no = tkinter.Radiobutton(master = self._open_frame,
                                   text = 'No',variable = self.open_var,
                                            value = "False", command = self.set_open_false,
                                   font = ('helvetica', 15), )
        
        
        self._open_no.pack()

        """ SET OPEN NOW AS DEFAULT"""
        self._open_yes.select()

        ##Buttons to make a search for one random restaurant
        search_one_button = tkinter.Button(
            master = self._root_window, text = ' Search for Random Restuarant ', font = DEFAULT_FONT,
            command = self.search_for_one)

        search_one_button.grid(row = 5, column = 1, padx = 10, pady = 10)

        """
        list_button = tkinter.Button(
            master = self._root_window, text = ' List Nearby Restaurants ', font = DEFAULT_FONT,
            command = self.list_rest)

        list_button.grid(row = 5, column = 2, padx = 10, pady = 10)
        """

        ##RESULTS
        """
        self._results_label = tkinter.Label(master = self._root_window,
                                   text = 'Results: ',
                                   font = DEFAULT_FONT)
        self._results_label.grid(row = 6, column = 0)

        #self._results_info
        """




        
    def run(self):
        self._root_window.mainloop()




    def set_open_true(self):
        self.open_var = "True"
        
    def set_open_false(self):
        self.open_var = "False"



        

    def search_for_one(self):
        location = self._find_input.get()
        near = self._location_input.get()

        ##If the fields are empty throw an exception
        if len(location) == 0 or len(near) == 0:
            raise EmptyFieldsError("FIELDS (Find or Near) are EMPTY!")
        
        #print(location)
        #print(near)
        #print(self.open_var)
        price_range_boxes = [self.price_1.get(), self.price_2.get(),
                             self.price_3.get(), self.price_4.get()]
        prices = price_list_to_string(price_range_boxes)
        #print(prices)

        rest = randomizer_parts.get_random_restaurant(near, prices, location, self.open_var)
        randomizer_parts.open_webpage(rest)

    def list_rest(self):
        location = self._find_input.get()
        near = self._location_input.get()

        ##If the fields are empty throw an exception
        if len(location) == 0 or len(near) == 0:
            raise EmptyFieldsError("FIELDS (Find or Near) are EMPTY!")
        
        #print(location)
        #print(near)
        #print(self.open_var)
        price_range_boxes = [self.price_1.get(), self.price_2.get(),
                             self.price_3.get(), self.price_4.get()]
        prices = price_list_to_string(price_range_boxes)
        #print(prices)

        rest = randomizer_parts.get_list_of_restaurants(near, prices, location, self.open_var)

def price_list_to_string(prices):
    copy = []
    for each in prices:
        if each != "":
            copy.append(each)
    return ",".join(copy)




screen = yelp_randomizer_search()
screen.run()
