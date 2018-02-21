from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    '''
    turn a simple dict of key/value pairs into xml.
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

if __name__ == '__main__':
    s = { 'name': 'WMT', 'shares': 100, 'price': 123.4 }
    e = dict_to_xml('stock', s)
    print(e)    # returns an Element instance

    # convert Element instance to a byte string using tostring() function
    from xml.etree.ElementTree import tostring
    print(tostring(e))
    
    # attach attributes to an element using the set() method
    e.set('_id', '1234')
    print(tostring(e))
    