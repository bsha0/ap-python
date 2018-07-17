# type 'pip install pypiwin32' to install if missing
import win32com.client
from enum import Enum


class Version(Enum):
    Default = ''
    V9 = '.35.0'
    V10 = '.36.0'


class HAPAttributeNumber(Enum):
    HAP_UNITROW = 2
    HAP_UNITCOL = 3


class Application(object):
    def __init__(self, version=Version.Default):
        self.__ihapp = win32com.client.Dispatch('Apwn.Document'+version.value)
        self.__ihapp.SuppressDialogs = True

    def open_file(self, path):
        self.__ihapp.InitFromArchive2(path, 0)
        self.__ihRoot = self.__ihapp.Application.Tree

    def run(self):
        self.__ihapp.Run2()

    def find_node(self, path):
        return self.__ihRoot.FindNode(path)

    def print_streams(self):
        streams = []
        node = self.find_node(r'\Data\Streams')
        for item in node.Elements:
            streams.append(item.Name)
        return tuple(streams)

    def print_blocks(self):
        blocks = []
        node = self.find_node(r'\Data\Blocks')
        for item in node.Elements:
            blocks.append(item.Name)
        return tuple(blocks)

    def get_value(self, node, unit=None):
        return (node.value, node.UnitString)

    def set_value(self, node, value, unit=None):
        if unit is None:
            unitcol = node.AttributeValue(HAPAttributeNumber.HAP_UNITCOL.value)
        else:
            units = self.get_units(node)
            if unit in units:
                unitcol = units.index(unit) + 1
            else:
                raise Exception(f"Unit {unit} isn't in the available list {units}.")
        node.SetValueAndUnit(value, unitcol)

    def get_units(self, node):
        units = []
        row = node.AttributeValue(HAPAttributeNumber.HAP_UNITROW.value)
        if row > 0:
            for unit in self.find_node(r'\Unit Table').Elements(row - 1).Elements:
                units.append(unit.Name)
        return tuple(units)

    @property
    def visible(self):
        return self.__ihapp.Visible

    @visible.setter
    def visible(self, value):
        self.__ihapp.Visible = value


if __name__ == '__main__':
    pass
