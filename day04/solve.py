import pathlib
import os
import re
from dataclasses import dataclass
from functools import reduce

class Validations:
    @classmethod
    def value_between(cls, value, minimum, maximum):
        return minimum <= value <= maximum

    @classmethod
    def valid_year(cls, year, minimum, maximum, length):
        return re.match("[0-9]{4}$", str(year)) is not None\
                and cls.value_between(year, minimum, maximum)
    @classmethod
    def is_valid_byr(cls, byr):
        return cls.valid_year(int(byr), 1920, 2002, 4)
    
    @classmethod
    def is_valid_iyr(cls, iyr):
        return cls.valid_year(int(iyr), 2010, 2020, 4)

    @classmethod
    def is_valid_eyr(cls, eyr):
        return cls.valid_year(int(eyr), 2020, 2030, 4)

    @classmethod
    def is_valid_hgt(cls, hgt):
        if not hgt.endswith("cm") and not hgt.endswith("in"):
            # print(f"Not valid hgt {hgt}")
            return False
        
        if hgt.endswith("cm") and\
                not cls.value_between(int(hgt.replace("cm","")), 150, 193):
            # print(f"Not valid hgt {hgt}")
            return False
        elif hgt.endswith("in") and\
                not cls.value_between(int(hgt.replace("in","")), 59, 76):
            # print(f"Not valid hgt {hgt}")
            return False
        return True
        
    @classmethod
    def is_valid_hcl(cls, hcl):
        return re.match("^#[0-9a-f]{6}$", hcl)

    @classmethod
    def is_valid_ecl(cls, ecl):
        return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    @classmethod
    def is_valid_pid(cls, pid):
        return re.match("^[0-9]{9}$", pid)

@dataclass
class Passport(object):
    """
    Args:
        object ([type]): [description]
    """
    byr:int = None #  byr (Birth Year)
    iyr:int = None #  iyr (Issue Year)
    eyr:int = None #  eyr (Expiration Year)
    hgt:str = None #  hgt (Height)
    hcl:str = None #  hcl (Hair Color)
    ecl:str = None #  ecl (Eye Color)
    pid:str = None #  pid (Passport ID)
    cid:int = None #  cid (Country ID)
    
    def is_valid(self):
        mandatory_fields = ["byr", "iyr","eyr", "pid", "ecl", "hcl", "hgt"]
        is_valid = reduce(
            lambda x, y : x and y, 
            map(lambda field: getattr(self, field) is not None, mandatory_fields))
        return is_valid

    def is_valid_p2(self):
        if not self.is_valid():
            return False       
        
        if not Validations.is_valid_byr(self.byr):
            # print(f"Not valid byr {self.byr}")
            return False
        
        if not Validations.is_valid_iyr(self.iyr):
            # print(f"Not valid iyr {self.iyr}")
            return False        
        
        if not Validations.is_valid_eyr(self.eyr):
            # print(f"Not valid eyr {self.eyr}")
            return False
        
        if not Validations.is_valid_hgt(self.hgt):
            # print(f"Not valid hgt {self.hgt}")
            return False
        
        if not Validations.is_valid_hcl(self.hcl):
            # print(f"Not valid hcl {self.hcl}")
            return False
        
        if not Validations.is_valid_ecl(self.ecl):
            # print(f"Not valid ecl {self.ecl}")
            return False

        if not Validations.is_valid_pid(self.pid):
            # print(f"Not valid pid {self.pid}")
            return False

        return True

def get_lines(file_path):
    with open(os.path.join(pathlib.Path().absolute(),file_path)) as fh:
        line = {}
        current_line = fh.readline()
        while len(current_line) != 0:
            if current_line == "\n":
                yield Passport(**line)
                line = {}
            else:
                line.update({x.split(":")[0]:x.split(":")[1] for x in current_line.strip().split(" ")})
            current_line = fh.readline()
        yield Passport(**line)

print("---------- P1 ------------")
examples_validations = [passport.is_valid() for passport in get_lines("day04/example")]
assert examples_validations[0]
assert not  examples_validations[1]
assert  examples_validations[2]
assert not  examples_validations[3]
sol1 = sum([passport.is_valid() for passport in get_lines("day04/input")])
print(f"Sol 1: {sol1}")
    

print("---------- valid --------")
assert (sum([passport.is_valid_p2() for passport in get_lines("day04/valid")])) == 4

print("---------- invalid -------")
assert (sum([not passport.is_valid_p2() for passport in get_lines("day04/invalid")])) == 4

print("------- assertions -------")
assert Validations.is_valid_byr("2002")
assert not Validations.is_valid_byr("2003")

assert Validations.is_valid_hgt("60in")
assert Validations.is_valid_hgt("190cm")
assert not Validations.is_valid_hgt("190in")
assert not Validations.is_valid_hgt("190")

assert Validations.is_valid_hcl("#123abc")
assert not Validations.is_valid_hcl("#123abz")
assert not Validations.is_valid_hcl("123abc")

assert Validations.is_valid_ecl("brn")
assert not Validations.is_valid_ecl("wat")

assert Validations.is_valid_pid("000000001")
assert not Validations.is_valid_pid("0123456789")

print("---------- P2 ------------")
examples_validations = [passport.is_valid() for passport in get_lines("day04/example")]
assert examples_validations[0]
assert not  examples_validations[1]
assert  examples_validations[2]
assert not  examples_validations[3]
sol2 = sum([ passport.is_valid_p2() for passport in get_lines("day04/input")])
print(f"Sol 2: {sol2}")
    