from greww.data.json.json_utils import (make_json,
                                        feed_json,
                                        count_json,
                                        unfeed_json,
                                        read_json,
                                        search_json,
                                        jsonize_kwargs,
                                        _replace_json)
from greww.data.basics import remove_file, check_file
from greww._envs import GREWW_CACHE

JF = 'jf.json'

__data_frame_1 = {
    "hello" : "wait",
    "hella" : 33,
    "helli" : {
        "vroum" : ['broum',
                    'kroum'],
    },
}

__data_frame_2 = [
    {
        "num" : "a1",
        "age" : 3,
    },
    {
        "num" : "a2",
        "age" : 44
    },
    {
        "num" : "a3",
        "age" : 13,
    },
]

__micro_frame = {
    "num" : "a4",
    "age" : 3,
}

_args = (GREWW_CACHE, JF)

def test_json_file_basics():
    make_json(*_args, from_data=__data_frame_1, pretty=True)
    check_file(*_args)
    cn = count_json(*_args)
    assert cn == 3
    ct = read_json(*_args)
    assert __data_frame_1 == ct
    _replace_json(*_args, __data_frame_2)
    ct = read_json(*_args)
    assert ct == __data_frame_2
    remove_file(GREWW_CACHE, 'jf.json')

def test_json_operations():
    make_json(*_args, from_data=__data_frame_2, pretty=True)
    feed_json(*_args, __micro_frame)
    cn = count_json(*_args)
    assert cn == 4
    res = search_json(*_args, age=3)
    assert len(res) == 2
    assert res[0]['num'] == 'a1'
    assert res[1]['num'] == 'a4'
    unfeed_json(*_args, age=44)
    unfeed_json(*_args, num='a3')
    cn = count_json(*_args)
    assert cn == 2
    ct = read_json(*_args)
    assert ct[0]['num'] == 'a1'
    assert ct[1]['num'] == 'a4'
    remove_file(GREWW_CACHE, 'jf.json')

__all__ = [test_json_file_basics,
           test_json_operations]
