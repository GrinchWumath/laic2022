# laic2022
## 1.数据集标注格式：BIO,标签为：
     "O", "B-Defendants_vehicle", "I-Defendants_vehicle",
		 "B-defendants_driving_conditions","I-defendants_driving_conditions",
		 "B-Violations_of_the_defendant", "I-Violations_of_the_defendant",
		 "B-Place_of_action", "I-Place_of_action",
         "B-Name_of_carrier", "I-Name_of_carrier",
		 "B-Other_participants", "I-Other_participants",
		 "B-Participants_vehicle", "I-Participants_vehicle",
		 "B-driving_conditions_of_the_participant", "I-driving_conditions_of_the_participant",
		 "B-Violations_by_participants", "I-Violations_by_participants",
		 "B-Identification_of_defendants_responsibility", "I-Identification_of_defendants_responsibility",
		 "B-Identification_of_participants_responsibility", "I-Identification_of_participants_responsibility",
		 "B-Summary_of_the_defendants_conduct", "I-Summary_of_the_defendants_conduct"
## 2.需要更改的配置：
### 1.laic20022/data/path.py 中的路径
### 2.laic2022/model/path.py中的路径
### 3.需要把预训练模型文件夹放入model/bert文件夹中，本模型使用预训练模型下载地址https://gitcode.net/mirrors/ymcui/chinese-bert-wwm?utm_source=csdn_github_accelerator
### 4.train.py中的文件路径需要更改
### 5.train_helper.py中可以增加评价指标，以及绘制图标
### 6.main.py中的模型选择有"bilstm","bilstm-crf","bert-bilstm-crf",修改对应参数即可
