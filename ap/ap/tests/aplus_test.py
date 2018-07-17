import ap.aspenplus as aplus
import os

def main():
    ap = aplus.Application()
    ap.open_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pfdtut.bkp'))
    # set visible
    ap.visible = True
    # temperature of stream 1
    path = r'\Data\Streams\1\Input\TEMP\MIXED'
    node = ap.find_node(path)
    print(f'units: {ap.get_units(node)}')
    print(f'value: {ap.get_value(node)}')
    print(f'value of unit R: {ap.get_value(node, "R")}')
    ap.set_value(node, 500.0)
    print(f'value: {ap.get_value(node)}')
    ap.set_value(node, 500.0, 'R')
    print(f'value: {ap.get_value(node, "R")}')
    

if __name__ == '__main__':
    main()

