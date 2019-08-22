local _M = 
{
    title = 'Sequence',
    topics = {
        {
            title = 'InitTeachAction',
            markers = {'task-done',
            },
            note = {unitId=100186,bg_scene="bg_all/bg_1.csb",bg_objects={{name="clothes.clothes_1",initAnim="idle_1"},{name="clothes.clothes_2",initAnim="idle_1"},{name="clothes.clothes_3",initAnim="idle_1"},{name="clothes.socks_1",initAnim="idle_1"},{name="clothes.socks_2",initAnim="idle_1"},{name="food.egg",initAnim="idle_1"},{name="food.tomato",initAnim="idle_1"},{name="food.vegetables",initAnim="idle_1"},{name="food.yogurt",initAnim="idle_1"},{name="pillow.pillow_1",initAnim="idle_1"},{name="armoire",initAnim="idle_1",container=""},{name="sofa",initAnim="idle_1"},{name="ice_box",initAnim="idle_1"}}},
            id = '0s44oiv5kc8uihb7cansg3uj4r',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            label = '语音讲解',
            note = {voice="xxx.mp3",desc="播放语音讲解",},
            id = '2rlp53moqk6m2su3pvhqmufe3m',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            label = '小朋友，家里太乱了！快来帮忙整理一下房间吧！',
            note = {voice="xxx.mp3",desc="小朋友，家里太乱了！快来帮忙整理一下房间吧！",},
            id = '4r10dc5j3dusu8m67edagq2n2n',
        },
        {
            title = 'Parallel',
            topics = {
                {
                    title = 'VoiceAction',
                    markers = {'symbol-right',
                    },
                    label = '先拖动抱枕吧。',
                    note = {voice="xxx.mp3",desc="先拖动抱枕吧。",},
                    id = '5d5kboqb03h07l2cu51673j56s',
                },
                {
                    title = 'AMoveObjAction',
                    markers = {'task-done',
                    },
                    label = '抱枕拖到沙发上',
                    note = {moveSet={{"pillow.pillow_1","sofa","pillow.pillow_1"},},},
                    id = '1b2v4anjjbsitnt8n6bi0epn5l',
                },
            },
            markers = {'c_symbol_contact',
            },
            label = '控制：并行节点',
            id = '1ekmq7q2sk5cjgtcn933n49s2g',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            note = {voice="xxx.mp3",desc="快把房间里其他物品都分类整理好吧！想一想，食物应该放在哪里？",},
            id = '5b7psm0loknb6vplq1j4ith5ca',
        },
        {
            title = 'Parallel',
            topics = {
                {
                    title = 'AMoveObjAction',
                    markers = {'task-done',
                    },
                    note = {moveSet={{"food.egg","ice_box","food.egg"},{"food.tomato","ice_box","food.tomato"},{"food.vegetables","ice_box","food.vegetables"},{"food.yogurt","ice_box","food.yogurt"},},right={signal={key="moveTag",value=1},},},
                    id = '5fcgj6jpljbppmfjbdfdlttg5f',
                },
                {
                    title = 'Sequence',
                    topics = {
                        {
                            title = 'BlockTreeAction',
                            markers = {'symbol-right',
                            },
                            note = {signal="moveTag",value=1},
                            id = '229lg3kh3frg0rlt9hcvjkmp67',
                        },
                        {
                            title = 'VoiceAction',
                            markers = {'symbol-right',
                            },
                            label = '移动一个语音：正确，食物都放进冰箱里！',
                            note = {voice="xxx.mp3",desc="正确，食物都放进冰箱里！",runTag=1,},
                            id = '3cmui1n6fbur9eg9v0irlrph0l',
                        },
                    },
                    markers = {'people-blue',
                    },
                    label = '控制：顺序节点',
                    id = '6bdeve878mhc7a7to140il6csg',
                },
            },
            markers = {'c_symbol_contact',
            },
            label = '控制：并行节点',
            id = '7sn4ap7ckjbdkdjv0l23bj2o37',
        },
        {
            title = 'AnimAction',
            markers = {'symbol-right',
            },
            label = '冰箱门自动关上',
            note = {nodeName="ice_box",animName="right_1",isLoop=false,},
            id = '1l5bks4jjjqi6ifsbr7csbsabh',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            note = {voice="xxx.mp3",desc="衣服应该放在哪里？"},
            id = '4nqdidbn9p197o0ujv8o6u3fd7',
        },
        {
            title = 'Parallel',
            topics = {
                {
                    title = 'AMoveObjAction',
                    markers = {'task-done',
                    },
                    note = {moveSet={{"clothes.clothes_1","armoire","clothes.clothes_1"},{"clothes.clothes_2","armoire","clothes.clothes_2"},{"clothes.clothes_3","armoire","clothes.clothes_3"},{"clothes.socks_1","armoire","clothes.socks_1"},{"clothes.socks_2","armoire","clothes.socks_2"},},right={anim="right_1",idle="right_2",signal={key="moveTag",value=1},},},
                    id = '7ovng9cj7698ovuck0imtsv4tu',
                },
                {
                    title = 'Sequence',
                    topics = {
                        {
                            title = 'BlockTreeAction',
                            markers = {'symbol-right',
                            },
                            note = {signal='moveTag',value=1},
                            id = '50fipdddkq4jvgubkgesstjbav',
                        },
                        {
                            title = 'VoiceAction',
                            markers = {'symbol-right',
                            },
                            label = '移动一个语音：正确，食物都放进冰箱里！',
                            note = {voice="xxx.mp3",desc="正确，衣服都放进衣柜里！",},
                            id = '3m1ei8ainnjve3mvdvc7e0tohq',
                        },
                    },
                    markers = {'people-blue',
                    },
                    label = '控制：顺序节点',
                    id = '1h3etqg5fbgf90sojk50sn8ut3',
                },
            },
            markers = {'c_symbol_contact',
            },
            label = '控制：并行节点',
            id = '1mcu44ouea38uhjkekfl04pe6i',
        },
        {
            title = 'AnimAction',
            markers = {'symbol-right',
            },
            label = '衣柜柜门自动关上',
            note = {nodeName="armoire",animName="right_1",isLoop=false,},
            id = '0mcp4pjdh0510c40tinem9ggcm',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            label = '太棒啦！房间一下子整洁了，像这样，把物品按照相同的特征整理好，叫做分类。',
            note = {voice="xxx.mp3",desc="太棒啦！房间一下子整洁了，像这样，把物品按照相同的特征整理好，叫做分类。",},
            id = '6th2oej0io8q05gt0i3vp0c3oq',
        },
    },
    markers = {'people-blue',
    },
    label = 'root',
    id = '6uev5smjkkuul7ac6gvpb8rpks',
}

return _M