import 'antd/dist/antd.css';
import React from 'react';

import CustomLayout from "./containers/layout";
import ArticleList from "./containers/ArticleListView";

function App() {
  return (
    <div className="App">
      <CustomLayout>
        <ArticleList />
      </CustomLayout>
    </div>
  );
}

export default App;
