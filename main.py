from train.train import Train
from tools.get_ner_level_acc import precision

if __name__ == "__main__":
    use_pretrained_w2v = True
    model_type = "bilstm-crf"

    model_train = Train()
    model_train.train(use_pretrained_w2v=use_pretrained_w2v, model_type=model_type)

    text = "经审理查明：2017年8月30日凌晨，被告人谢某2饮酒后驾驶一辆车牌号为粤U号小型轿车沿潮州市潮安区彩庵线自南往北方向行驶，当车行驶至彩塘镇新联路段处时，因被告人谢某2疏忽大意，没有按照操作规范安全驾驶，致使车辆失控碰撞到由被害人郑某1驾驶并停放于道路东侧停车线内的粤U号轻型普通货车，后又碰撞到被害人谢某1、林某1停放在该处人行道上的二辆无号牌二轮摩托车，致摩托车在倒地过程中再次碰撞到正在该处路边吃宵夜的被害人谢某1、许某1、杨某，造成被告人谢某2及被害人谢某1、许某1、杨某受伤及四车不同程度受损的交通事故。事故发生后，谢某2、谢某1、许某1、杨某被送往医院治疗，后民警委托医护人员提取被告人谢某2的血样送检。经某政府2鉴定：送检的谢某2的血液中检出乙醇（Ethanol）成分，含量为215"

    result = model_train.predict(text, use_pretrained_w2v, model_type)
    print(result[0])

    result_dic = model_train.get_ner_list_dic(text, use_pretrained_w2v, model_type)
    print(result_dic)