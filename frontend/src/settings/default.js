import axios from 'axios';

let dev_url = 'http://127.0.0.1:8000';
let qas_url = 'http://54.180.118.173:8000';
let prd_url = 'http://54.180.118.173:8000';
const gv_app = {
    app_name: '(주) 도울정보기술',
    app_url: dev_url,
    app_type: "L",
};

/**
 * Url 설정
 *      L : 로컬
 *      Q : 교육
 *      P : 운영
 */
if (window.location.href.indexOf('localhost') > -1){
    gv_app.app_url = dev_url;
    gv_app.app_type = "L";
}else if (window.location.href.indexOf('54.180.118.173') > -1 || window.location.href.indexOf('ec2-54-180-118-173.ap-northeast-2.compute.amazonaws.com') > -1){
    gv_app.app_url = qas_url;
    gv_app.app_type = "Q";
}else if (window.location.href.indexOf('localhost') > -1){
    gv_app.app_url = prd_url;
    gv_app.app_type = "P";
}else{
    gv_app.app_url = dev_url;
    gv_app.app_type = "L";
}

export function search(url) {
    return axios.get(gv_app.app_url+url);
}

export function getData(data){
    const listData = [];  
    console.log(data)      
    const list = data.map(
        info => (
            listData.push(info)
        )
    );  
    return listData;
}

export function saveData(data, model){    
    return axios({
        method:"post",
        url: gv_app.app_url+"/"+model+"/save/",
        data: data
    });
}

export function deleteData(data, model){    
    return axios({
        method:"delete",
        url: gv_app.app_url+"/"+model+"/save/",
        data: data
    });
}

export { gv_app }