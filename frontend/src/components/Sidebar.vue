<template>
  <a-menu
    id="dddddd"
    v-model:openKeys="openKeys"
    v-model:selectedKeys="selectedKeys"
    style="width: 256px"
    mode="inline"
    @click="handleClick"
  >
    <a-sub-menu key="sub1" @titleClick="titleClick">
      <template #icon>
        <AppstoreOutlined />
      </template>
      <template #title>Tables</template>
      <a-menu-item key="1" @click="sendApiUrl1">CDC_CONN</a-menu-item>
      <a-menu-item key="2" @click="sendApiUrl2">CDC_FIELDS</a-menu-item>
      <a-menu-item key="3" @click="sendApiUrl3">CDC_STATUS</a-menu-item>
      <a-menu-item key="4" @click="sendApiUrl4">CDC_TABLES</a-menu-item>
     
    </a-sub-menu>
    <a-sub-menu key="sub2">
      <template #icon>
        <SettingOutlined />
      </template>
      <template #title>Settings</template>
      <a-menu-item key="9">Option 9</a-menu-item>
      <a-menu-item key="10">Option 10</a-menu-item>
      <a-menu-item key="11">Option 11</a-menu-item>
      <a-menu-item key="12">Option 12</a-menu-item>
      <a-sub-menu key="sub3" title="Submenu">
        <a-menu-item key="7">Option 7</a-menu-item>
        <a-menu-item key="8">Option 8</a-menu-item>
      </a-sub-menu>
    </a-sub-menu>
    <a-sub-menu key="sub3">
      <template #icon>
        <MailOutlined />
      </template>
      <template #title>FAQ</template>
      <a-menu-item key="9">Option 9</a-menu-item>
      <a-menu-item key="10">Option 10</a-menu-item>
      <a-menu-item key="11">Option 11</a-menu-item>
      <a-menu-item key="12">Option 12</a-menu-item>
    </a-sub-menu>
    <!-- <a-sub-menu key="sub1" @titleClick="titleClick">
      <template #icon>
        
      </template>
      <template #title>Navigation One</template>
      <a-menu-item-group key="g1">
        <template #icon>
          <QqOutlined />
        </template>
        <template #title>Item 1</template>
        <a-menu-item key="1">Option 1</a-menu-item>
        <a-menu-item key="2">Option 2</a-menu-item>
      </a-menu-item-group>
      <a-menu-item-group key="g2" title="Item 2">
        <a-menu-item key="3">Option 3</a-menu-item>
        <a-menu-item key="4">Option 4</a-menu-item>
      </a-menu-item-group>
    </a-sub-menu> -->
  </a-menu>
</template>
<script>

/* eslint-disable */
import { defineComponent, ref, watch } from 'vue';

import { MailOutlined, QqOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons-vue';
import store from '@/store';
export default defineComponent({
  // props: {
  //     apiUrl: ['CdcConn/', 'CdcFields/']
  // },
  methods: {
    
  },
  components: {
    MailOutlined,
    QqOutlined,
    AppstoreOutlined,
    SettingOutlined,
  },
/* eslint-enable */

  setup() {
    // const apiUrl = ['CdcConn/', 'CdcFields/']
    const selectedKeys = ref(['1']);
    const openKeys = ref(['sub1']);
    const handleClick = () => {
      // console.log('click', e);
    };
    const titleClick = e => {
      console.log('titleClick', e);
    };
    // const sendApiUrl2 = () => {
    //   store.commit('changeApiUrl', 'CdcFields/')
    //   console.log(store.state.localdata.apiUrl + ' this comes from changeApiUrl')
    // };
    watch(() => openKeys, val => {
      console.log('openKeys', val);
      
    });
    // watch(() => {
    //   store.state.localdata.apiUrl
    // });
    const sendApiUrl1 = () => {
      store.commit('changeApiUrl', 'CdcConn/')
      store.commit('enableDataDelete')
      store.commit('disableDataAdd')
      store.dispatch('getData', store.state.localdata.apiUrl)
      // console.log(store.state.localdata.data)
    }
    
    const sendApiUrl2 = () => {
      store.commit('changeApiUrl', 'CdcFields/')
      store.dispatch('getData', store.state.localdata.apiUrl).then(() => {
        // console.log(store.state.localdata.data)
      })
      store.commit('disableDataDelete')
      store.commit('disableDataAdd')
    }
    const sendApiUrl3 = () => {
      store.commit('changeApiUrl', 'CdcStatus/')
      store.dispatch('getData', store.state.localdata.apiUrl)
      store.commit('disableDataDelete')
      store.commit('disableDataAdd')
      // console.log(store.state.localdata.apiUrl)
    }
    const sendApiUrl4 = () => {
      store.commit('changeApiUrl', 'CdcTables/')
      store.dispatch('getData', store.state.localdata.apiUrl)
      store.commit('disableDataDelete')
      store.commit('enableDataAdd')
      // console.log(store.state.localdata.apiUrl)
    }
    return {
      selectedKeys,
      openKeys,
      handleClick,
      titleClick,
      sendApiUrl1,
      sendApiUrl2,
      sendApiUrl3,
      sendApiUrl4
      // sendApiUrl2,
      // apiUrl
    };
  },
});
</script>