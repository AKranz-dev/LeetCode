class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32
        ans.append(kelvin)
        ans.append(fahrenheit)

        return ans


