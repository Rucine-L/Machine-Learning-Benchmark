<template>
<div class="container">
    
    <card 
        class="type-card"
        :id=0
        :title="title_" 
        :options="option_" 
        :isMultiple="IsMultiple_" 
        :explain="explain_"
        @type-selected="handleTypeSelected" />
    
    <card 
        v-for="item in items" 
        :key="item.id" 
        :id="item.id"
        :title="item.title" 
        :options="item.option" 
        :isMultiple="item.IsMultiple" 
        :explain="item.explain"
        @option-selected="handleOptionSelected" />

    <run 
        :res="result" 
        @click-send="handleSend" />
      
</div>
</template>
    
<script>
import card from "./components/card.vue";
import run from "./components/run.vue";

export default{
    data(){
        return{
            title_:"问题类型",
            explain_: "选择问题类型",
            option_: ["分类问题","回归问题"],
            IsMultiple_: false,

            titles: ["数据集选择", "数据分割比例", "数据分割器", "模型学习率", "训练模型", "评估指标"],
            explains: ["选择一个数据集","选择训练集和测试机的比例","选择分割器的类型","选择学习率","选择一个模型","可选择多个指标"],
            options: [],
            IsMultiple: false,
            items: [],

            result:[],
            
            //问题类型:0分类 1回归
            problem_type:0,
            // 保存合并后的选项值的数组
            mergedSelection: [] ,

            websocket: null,
        }
    },
    components:{
        card,
        run,
    },
    methods: {
        //重新计算items值
        updateItems() {

            this.items = this.titles.map((title, index) => ({
                id: index + 1,
                title,
                explain: this.explains[index],
                option: this.options[index],
                isMultiple: this.IsMultiple
                }));
            this.items[5].IsMultiple=true
            
        },
        handleOptionSelected(selection,id) {
            // 接收子组件传递的选项值
            this.mergedSelection[id-1]=selection;
            //console.log(this.mergedSelection)
        },
        handleTypeSelected(selection){
            if(selection==this.option_[0])
                this.problem_type=0;
            else 
                this.problem_type=1;
            this.websocket.send(this.problem_type);
        },
        handleSend() {
            if (this.mergedSelection.length === 6 && this.mergedSelection.every(selection => selection !== null)) {
                // 发送消息给后端
                console.log(this.mergedSelection);
                this.websocket.send(JSON.stringify(this.mergedSelection));
            }  
            else
                alert('数据不完整');
        },
    },
    mounted() {
        this.updateItems();
        // 在组件挂载时，创建WebSocket对象并建立连接
        this.websocket = new WebSocket('ws://127.0.0.1:8080');

        // 监听WebSocket连接状态变化
        this.websocket.onopen = () => {
            alert('已连接');
        };

        // 监听接收到的消息
        this.websocket.onmessage = (event) => {
            const message=JSON.parse(event.data);
            if(message.id==1){
                this.options=message.keys;
                this.updateItems();
            }
            else{
                this.result=message.res;
            }
        };
    },
}
</script>
    
<style scoped>
.container{
    position: relative;
    width: 1200px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    z-index: 1;
}
.type-card {
    position: relative;
    width: 1000px;
    height: 220px;
}
</style>
    