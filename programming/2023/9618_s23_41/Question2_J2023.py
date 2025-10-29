class Vehicle:
    def __init__(self, pID, pMaxSpeed, pIncreaseAmount):
        self.__ID = pID  # PRIVATE, STRING
        self.__MaxSpeed = pMaxSpeed  # PRIVATE, INTEGER
        self.__IncreaseAmount = pIncreaseAmount  # PRIVATE, INTEGER
        self.__CurrentSpeed = 0  # PRIVATE, INTEGER
        self.__HorizontalPosition = 0  # PRIVATE, INTEGER

    def GetCurrentSpeed(self):  # returns INTEGER
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):  # returns INTEGER
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):  # returns INTEGER
        return self.__HorizontalPosition

    def GetMaxSpeed(self):  # returns INTEGER
        return self.__MaxSpeed

    def SetCurrentSpeed(self, pSpeed):
        self.__CurrentSpeed = pSpeed

    def SetHorizontalPosition(self, pPosition):
        self.__HorizontalPosition = pPosition

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if (self.__CurrentSpeed > self.__MaxSpeed):
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, pVerticalChange, pMaxHeight, pID, pMaxSpeed, pIncreaseAmount):
        super().__init__(pID, pMaxSpeed, pIncreaseAmount)
        self.__VerticalChange = pVerticalChange  # PRIVATE, INTEGER
        self.__MaxHeight = pMaxHeight  # PRIVATE, INTEGER
        self.__VerticalPosition = 0  # PRIVATE, INTEGER

    def IncreaseSpeed(self):
        current_speed = self.GetCurrentSpeed()
        increase_amount = self.GetIncreaseAmount()
        horizontal_position = self.GetHorizontalPosition()
        max_speed = self.GetMaxSpeed()

        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange

        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        current_speed = current_speed + increase_amount

        if current_speed > max_speed:
            current_speed = max_speed

        horizontal_position = horizontal_position + current_speed

        self.SetCurrentSpeed(current_speed)
        self.SetHorizontalPosition(horizontal_position)

    def GetVerticalPosition(self):  # returns INTEGER
        return self.__VerticalPosition

def VehicleTelemetry(pVehicle):
    print(f"The speed is {pVehicle.GetCurrentSpeed()}")
    print(f"The horizontal position is {pVehicle.GetHorizontalPosition()}")
    if str(type(pVehicle)) == "<class '__main__.Helicopter'>":
        print(f"The vertical position is {pVehicle.GetVerticalPosition()}")


car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter(3, 100, "Lion", 350, 40)

car.IncreaseSpeed()
car.IncreaseSpeed()
VehicleTelemetry(car)

helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
VehicleTelemetry(helicopter)
