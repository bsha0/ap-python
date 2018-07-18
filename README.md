# Description
python automation packgae for aspen plus and aspen hysys.

# installation
## 'pip install ap-python'

# How to use it?
## aspen plus
''' python

    import ap_python.aspenplus as aplus
    import os

    ap = aplus.Application()
    ap.open_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pfdtut.bkp'))
    # set visible
    ap.visible = True
    print(f'streams: {ap.print_streams()}')
    print(f'blocks: {ap.print_blocks()}')
    # temperature of stream 1
    path = r'\Data\Streams\1\Input\TEMP\MIXED'
    node = ap.find_node(path)
    print(f'units: {ap.get_units(node)}')
    print(f'value: {ap.get_value(node)}')
    print(f'value for unit R: {ap.get_value(node, "R")}')
    ap.set_value(node, 500.0)
    print(f'value: {ap.get_value(node)}')
    ap.set_value(node, 500.0, 'R')
    print(f'value: {ap.get_value(node, "R")}')
    ap.saveas(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pfdtut1.bkp'))
    ap.close()

## aspen hysys
''' python

    import ap_python.aspenhysys as hysys
    import os

    hy = hysys.Application()
    hy.open_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Atmospheric Crude Tower.hsc'))
    # set visible
    hy.visible = True

    # temperature of stream 'Raw Crude'
    path = r'FlowSht.1/StreamObject.400(Raw Crude):Temperature.502.0'
    node = hy.find_node(path)
    print(f'units: {hy.get_units(node)}')
    print(f'value: {hy.get_value(node)}')
    print(f'value for unit R: {hy.get_value(node, "R")}')
    hy.set_value(node, 500.0)
    assert(hy.get_value(node)[0] == 500.0)
    print(f'value: {hy.get_value(node)}')
    hy.set_value(node, 500.0, 'R')
    assert(hy.get_value(node, 'R')[0] == 500.0)
    print(f'value: {hy.get_value(node, "R")}')
    hy.saveas(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Atmospheric Crude Tower1.hsc'))
    hy.close()

