import React, { useState, useEffect } from 'react';
import MaterialTable from 'material-table';
import axios from 'axios';
import * as service from '../settings/default';

function MaterialTableDemo(props) {
  
  const [state, setState] = useState({
    columns: [],
    data: [],
    // data: [
    //   { name: 'Mehmet', surname: 'Baran', birthYear: 1987, birthCity: 63 },
    //   {
    //     name: 'Zerya Betül',
    //     surname: 'Baran',
    //     birthYear: 2017,
    //     birthCity: 34,
    //   },
    // ],
  });  

  // componentDidMount, componentDidUpdate와 비슷합니다
  useEffect(() => {    
    console.log('마운트 될 때만 실행됩니다.');  
    setState(prevState => {
        const data = props.source;                /** 데이터*/
        const columns = props.columns;            /** 컬럼명*/
        return { ...prevState, data, columns };
    });
  },[]);

  const callSearchApi = () => {
    const data = service.search(props.search).then(res => {             
      setState(prevState => {
          const data = res.data;                /** 데이터*/
          return { ...prevState, data };
      }); 			
    });
  };
  
  return (
    <MaterialTable
      title={props.title}
      columns={state.columns}
      data={state.data}
      editable={{
        onRowAdd: newData =>
          new Promise(resolve => {
            setTimeout(() => {
              resolve();
              setState(prevState => {
                const data = [...prevState.data];
                data.push(newData);
                return { ...prevState, data };                
              });

              service.saveData(newData,props.model).then(res => {
                callSearchApi();
              });   
              
            }, 600);
          }),
        onRowUpdate: (newData, oldData) =>          
          new Promise(resolve => {
            setTimeout(() => {
              resolve();
              if (oldData) {
                setState(prevState => {
                  const data = [...prevState.data];
                  data[data.indexOf(oldData)] = newData;
                  return { ...prevState, data };
                });

                service.saveData(newData,props.model).then(res => {
                  callSearchApi();
                });              
              }
            }, 600);
          }),
        onRowDelete: oldData =>
          new Promise(resolve => {
            setTimeout(() => {
              resolve();
              setState(prevState => {
                const data = [...prevState.data];
                data.splice(data.indexOf(oldData), 1);
                return { ...prevState, data };
              });

              service.deleteData(oldData,props.model).then(res => {
                callSearchApi();
              });                
            }, 600);
          }),
      }}
    />
  );
}

export default MaterialTableDemo;