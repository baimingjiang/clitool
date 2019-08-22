local _M = 
{
    title = 'Sequence',
    topics = {
        {
            title = 'InitTeachAction',
            markers = {'task-done',
            },
            note = {unitId=100186,bg_scene="bg_all/bg_2.csb",bg_objects={{name="shucai.ProjectNode_3",initAnim="idle_1",randomObj=1},{name="shucai.ProjectNode_7",initAnim="idle_1",randomObj=1},{name="shucai.ProjectNode_6",initAnim="idle_1",randomObj=1},{name="shucai.ProjectNode_5",initAnim="idle_1",randomObj=1},{name="shucai.ProjectNode_4",initAnim="idle_1",randomObj=1},{name="shuiguo.ProjectNode_18",initAnim="idle_1",randomObj=2},{name="shuiguo.ProjectNode_22",initAnim="idle_1",randomObj=2},{name="shuiguo.ProjectNode_21",initAnim="idle_1",randomObj=2},{name="shuiguo.ProjectNode_20",initAnim="idle_1",randomObj=2},{name="shuiguo.ProjectNode_19",initAnim="idle_1",randomObj=2},{name="plate.plate_1",path="plate/plate_1.csb",initAnim="idle_1"},{name="plate.plate_2",path="plate/plate_2.csb",initAnim="idle_1"},},randomObjs={{{name="vegetables_1",path="p3_food/vegetables_1.csb"},{name="vegetables_2",path="p3_food/vegetables_2.csb"},{name="vegetables_3",path="p3_food/vegetables_3.csb"},{name="vegetables_4",path="p3_food/vegetables_4.csb"},{name="vegetables_5",path="p3_food/vegetables_5.csb"},},{{name="fruit_6",path="p3_food/fruit_6.csb"},{name="fruit_7",path="p3_food/fruit_7.csb"},{name="fruit_8",path="p3_food/fruit_8.csb"},{name="fruit_9",path="p3_food/fruit_9.csb"},{name="fruit_10",path="p3_food/fruit_10.csb"},},}},
            id = '4hlbg3k7cel7vh61hjgnbsouf9',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            label = '小朋友，快用分类的本领。帮我把这些食物分类整理好吧！',
            note = {voice="xxx.mp3",},
            id = '3sj7fjlo4enmqg1n54aff30ecr',
        },
        {
            title = 'AMoveObjAction',
            markers = {'task-done',
            },
            note = {moveSet={{"fruit_6","plate.plate_1"},{"fruit_7","plate.plate_1"},{"fruit_8","plate.plate_1"},{"fruit_9","plate.plate_1"},{"fruit_10","plate.plate_1"},{"vegetables_1","plate.plate_2"},{"vegetables_2","plate.plate_2"},{"vegetables_3","plate.plate_2"},{"vegetables_4","plate.plate_2"},{"vegetables_5","plate.plate_2"},},},
            id = '24i2dspko562geb6dj3131lg5o',
        },
        {
            title = 'VoiceAction',
            markers = {'symbol-right',
            },
            label = '真厉害，你学会了分类哦。',
            note = {voice="xxx.mp3",},
            id = '1b7bvdofcm32n6jkbjf9c68skn',
        },
    },
    id = '55foluefa4o4emda0ao3j8p4n9',
}

return _M