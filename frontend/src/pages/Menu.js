import React, { Component, useState, useEffect } from 'react';
import Table from '../components/Table';
import axios from 'axios';
import '../styles/index.css';
import * as service from '../settings/default';
import CircularProgress from '@material-ui/core/CircularProgress';

class Main extends Component {
  constructor(props) {
      super(props);
      this.state = {
        data: [],
        model:"blog/menu",
        isloading: true,
        columns: [
          { title: 'name', field: 'name' },
          { title: 'code', field: 'code' },
          { title: 'menu_parent', field: 'menu_parent' },
          { title: 'link', field: 'link' },
          { title: 'level', field: 'level', type: 'numeric' },
          { title: 'sort', field: 'sort', type: 'numeric' },
        ]
      }
  }
  componentDidMount() {
		this.callSearchApi();
  }
  callSearchApi() {
    const data = service.search(`/${this.state.model}/sel/`).then(res => {       
      this.setState({data: res.data,isloading: false}); 			
    });
  }

  render() {
     if(this.state.isloading){ return(<div className="loading"><CircularProgress disableShrink /></div>)}
      return ( 
          <div>
            <Table
              source={this.state.data}
              columns={this.state.columns}
              title="조회화면"
              model={this.state.model}
              search={`/${this.state.model}/sel/`}
            />

          </div>
      )
  }
}


export default Main;


