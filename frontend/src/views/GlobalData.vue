<template>
  <div class="grid-container">
      <div class="grid-item1">
        <Navbar2></Navbar2>
      </div>
      <div class="grid-item2">
        <Sidebar></Sidebar>
      </div>
      <div class="grid-item3">
        <SearchField></SearchField>
      </div>
      <div class="grid-item4">
        <!-- Item-4 -->
        <!-- <step-backward-filled />
        <sliders-filled /> -->
      </div>
      <div class="grid-item5">
        <Suspense>
          <template #default>
            <local-data :api-url= apiUrl></local-data>
          </template>
          <template #fallback>
            <div>Loading...</div>
          </template>
        </Suspense>
        
      </div>
      <div class="grid-item6">
        <!-- Item-6 -->
      </div>
      <div class="grid-item7">
        <!-- Item-7 -->
      </div>
    <!-- </div> -->
  </div>
</template>
<script>

/* eslint-disable */
import Navbar2 from '@/components/Navbar2.vue'
import LocalData from '@/components/LocalData'
import Sidebar from '@/components/Sidebar.vue'
import SearchField from '@/components/SearchField.vue'
import { ref, computed, watchEffect } from 'vue'
import { useStore } from 'vuex'
// import store from '@/store'
export default {
  components: {
    Sidebar,
    SearchField,
    Navbar2,
    LocalData,
  },
  setup () {
    const store = useStore()
    console.log(store.state.localdata.apiUrl)
    const apiUrl = computed(() => store.state.localdata.apiUrl)
    console.log('apiUrl comes from GlobalData ' + apiUrl.value)
  // computed: {
  //   // apiUrl() {return this.$store.state.localdata.apiUrl}
  // },
  // mounted() {
  //   // this.$store.dispatch('getData', this.apiUrl)
  //   // this.$store.commit('changeApiUrl', this.apiUrl)
  // },
  // watch() {
  //   this.$store.state.localdata.apiUrl
  // }

    return {
      apiUrl,
      // apiUrl: computed(() => store.state.localdata.apiUrl)
    }
  }
  
}
/* eslint-enable */
</script>
<style lang="less">
.editable-cell {
  position: relative;
  .editable-cell-input-wrapper,
  .editable-cell-text-wrapper {
    padding-right: 24px;
  }

  .editable-cell-text-wrapper {
    padding: 5px 24px 5px 5px;
  }

  .editable-cell-icon,
  .editable-cell-icon-check {
    position: absolute;
    right: 0;
    width: 20px;
    cursor: pointer;
  }

  .editable-cell-icon {
    margin-top: 4px;
    display: none;
  }

  .editable-cell-icon-check {
    line-height: 28px;
  }

  .editable-cell-icon:hover,
  .editable-cell-icon-check:hover {
    color: #030c13;
  }

  .editable-add-btn {
    margin-bottom: 8px;
  }
}

.editable-cell:hover .editable-cell-icon {
  color: #030c13;
  display: inline-block;
}


.grid-container {
  display: grid;
  grid-template-columns: max-content auto minmax(150px, 200px);
  grid-template-rows: 40px 40px auto 40px;
  height: 100vh;
  width: 100%;
  // border: 2px solid rgb(197, 56, 21);
  gap: 2px
}

.grid-item {
  // border: 5px solid rgb(73, 100, 0);
}

// Navbar
.grid-item1 {
  /* position: fixed; */
  grid-column: 1/4;
  grid-row: 1/2;
  // background-color: rgba(165, 42, 42, 0.336);
}

// Sidebar
.grid-item2 {
  grid-column: 1/2;
  grid-row: 2/4;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
}

// SearchField
.grid-item3 {
  grid-column: 2/3;
  grid-row: 2/3;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
  display: block;
  padding: 3px;
}

.grid-item4 {
  grid-column: 3/4;
  grid-row: 2/3;
  background-color: white;
  box-shadow: 1px 1px 1px 0px rgba(0, 0, 0, 0.185);
}

.grid-item5 {
  padding: 5px;
  grid-column: 2/3;
  grid-row: 3/4;
  background-color: rgba(90, 85, 86, 0.075);
}

.grid-item6 {
  grid-column: 3/4;
  grid-row: 3/4;
  background-color: white;
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.185);
}

.grid-item7 {
  grid-column: 1/4;
  grid-row: 4/5;
  background-color: white;
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.185);
  // background-color: rgba(142, 165, 42, 0.336);
}




</style>