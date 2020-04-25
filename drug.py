class Drug:
    price_of_pack: int = 250

    def __init__(self, name_of_drug=None, how_to_use=None, volume_of_active_substance_in_mg=None, active_substance=None,
                 max_doses_per_day=None, quantity_in_box=None):
        self.name_of_drug = name_of_drug
        self.how_to_use = how_to_use
        self.volume_of_active_substance_in_mg = volume_of_active_substance_in_mg
        self.active_substance = active_substance
        self.max_doses_per_day = max_doses_per_day
        self.quantity_in_box = quantity_in_box

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return

    def __str__(self):
        name_of_drug = 'Name of Drug: {0}\n'.format(self.name_of_drug)
        how_to_use = 'How to Use: {0}\n'.format(self.how_to_use)
        volume_of_active_substance_in_mg = 'Volume of active substance in milligram:{0}\n'.format(
            self.volume_of_active_substance_in_mg)
        active_substance = 'Active substance:{0}\n'.format(self.active_substance)
        max_doses_per_day = 'Max Dose per Day: {0}\n'.format(self.max_doses_per_day)
        quantity_in_box = 'Quantity in box:{0}\n'.format(self.quantity_in_box)
        price_of_pack = 'Price of pack:{0}\n'.format(Drug.price_of_pack)
        return name_of_drug + how_to_use + volume_of_active_substance_in_mg + \
               active_substance + max_doses_per_day + quantity_in_box + price_of_pack

    @staticmethod
    def get_max_number_of_beds_in_room():
        return Drug.price_of_pack

    def get_name_of_drug(self):
        return self.name_of_drug

    def set_name_of_drug(self, name_of_drug):
        self.name_of_drug = name_of_drug

    def get_how_to_use(self):
        return self.how_to_use

    def set_how_to_use(self, how_to_use):
        self.how_to_use = how_to_use

    def get_volume_of_active_substance_in_mg(self):
        return self.volume_of_active_substance_in_mg

    def set_volume_of_active_substance_in_mg(self, volume_of_active_substance_in_mg):
        self.volume_of_active_substance_in_mg = volume_of_active_substance_in_mg

    def get_active_substance(self):
        return self.active_substance

    def set_active_substance(self, active_substance):
        self.active_substance = active_substance

    def get_max_doses_per_day(self):
        return self.max_doses_per_day

    def set_max_doses_per_day(self, max_doses_per_day):
        self.max_doses_per_day = max_doses_per_day

    def get_quantity_in_box(self):
        return self.quantity_in_box

    def set_quantity_in_box(self, quantity_in_box):
        self.quantity_in_box = quantity_in_box
