local _M = 
{
    title = 'Sequence',
    topics = {
        {
            title = 'InitTeachAction',
            markers = {'task-done',
            },
            note = {unitId=100186,bg_scene="bg_all/bg_3.csb",bg_objects={{name="conveyer_belt_1",initAnim="idle_1"},{name="frame_1",initAnim="idle_1"},{name="frame_2",initAnim="idle_1"},{name="frame_3",initAnim="idle_1"},{name="biscuit_1",container="biscuit",path="biscuit/biscuit_1.csb"},{name="biscuit_2",container="biscuit",path="biscuit/biscuit_2.csb"},{name="biscuit_3",container="biscuit",path="biscuit/biscuit_3.csb"},{name="biscuit_4",container="biscuit",path="biscuit/biscuit_4.csb"},{name="biscuit_5",container="biscuit",path="biscuit/biscuit_5.csb"},{name="biscuit_6",container="biscuit",path="biscuit/biscuit_6.csb"},{name="biscuit_7",container="biscuit",path="biscuit/biscuit_7.csb"},{name="biscuit_8",container="biscuit",path="biscuit/biscuit_8.csb"},{name="biscuit_9",container="biscuit",path="biscuit/biscuit_9.csb"},{name="biscuit_10",container="biscuit",path="biscuit/biscuit_10.csb"},{name="biscuit_11",container="biscuit",path="biscuit/biscuit_11.csb"},}},
            id = '6g0qii7rgij1pas8mto4ie1lp7',
        },
        {
            title = 'Parallel',
            topics = {
                {
                    title = 'Sequence',
                    topics = {
                        {
                            title = 'AnimAction',
                            markers = {'symbol-right',
                            },
                            note = {nodeName="conveyer_belt_1",animName="start_1",isLoop=true,},
                            id = '5c2b86jcrmrdhgdfj772f3lu5b',
                        },
                        {
                            title = 'BiscuitSortAction',
                            markers = {'symbol-right',
                            },
                            note = {randomSort={"biscuit_1","biscuit_2","biscuit_3","biscuit_4","biscuit_5","biscuit_6","biscuit_7","biscuit_8","biscuit_9","biscuit_10","biscuit_11",}},
                            id = '18di25hnqur171jenhqhmoait5',
                        },
                        {
                            title = 'BiscuitSlideAction',
                            markers = {'symbol-right',
                            },
                            note = {nodeName="conveyer_belt_1",animName="start_1",isLoop=true,},
                            id = '1f3sq6nk8e5vq6uo1f21p18bo0',
                        },
                    },
                    markers = {'people-blue',
                    },
                    label = '控制：顺序节点',
                    id = '26k2snssbhb0kuk8kjqoaeqme6',
                },
                {
                    title = 'Sequence',
                    topics = {
                        {
                            title = 'VoiceAction',
                            markers = {'symbol-right',
                            },
                            label = '请你来给饼干分类吧。',
                            note = {voice="xxx.mp3",desc="播放语音讲解",},
                            id = '1qfo3pagvkjl9pr8n9d4ssbfcq',
                        },
                        {
                            title = 'VoiceAction',
                            markers = {'symbol-right',
                            },
                            label = '小朋友，家里太乱了！快来帮忙整理一下房间吧！',
                            note = {voice="xxx.mp3",desc="小朋友，家里太乱了！快来帮忙整理一下房间吧！",},
                            id = '3i3jdlb79e75klmuqco30jevbm',
                        },
                        {
                            title = 'AMoveObjAction',
                            markers = {'task-done',
                            },
                            note = {moveSet={},right={signal={key="moveTag",value=1},},},
                            id = '4smnju3kct0apdip1cmd4mllbp',
                        },
                        {
                            title = 'VoiceAction',
                            markers = {'symbol-right',
                            },
                            label = '小朋友，今天学习简单的一维分类，你学会了吗？',
                            note = {voice="xxx.mp3",},
                            id = '2unioob9ja3smjq824vjvlfkvj',
                        },
                    },
                    markers = {'people-blue',
                    },
                    label = '控制：顺序节点',
                    id = '0u3bip1m7lqbcatvdaip7vulep',
                },
            },
            markers = {'c_symbol_contact',
            },
            label = '控制：并行节点',
            id = '759fdcu95ura45mdbue08bvgtm',
        },
    },
    markers = {'people-blue',
    },
    label = 'root',
    id = '1aimfgd3n0q3lie2afg7c2mfrb',
}

return _M