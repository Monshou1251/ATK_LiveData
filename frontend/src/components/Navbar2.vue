<template>
  <div class="flex-container">
    <div class="flex-item-logo">
        <img class="logo" src="@/assets/logo_big_ATK.png" alt="logo" />
    </div>
    <div class="flex-item item-2">
        <div><router-link class="nav-links" :to="{name: 'home'}" exact>Home</router-link></div>
        <div><router-link class="nav-links" :to="{name: 'datatable'}" exact>Datatable</router-link></div>
        <div><router-link class="nav-links" :to="{name: 'datatableelement'}" exact>DatatableElement</router-link></div>
        <div><router-link :to="{name: 'login'}" exact
            ><button class="header_button">Login</button></router-link
          ></div>
    </div>
  </div>
</template>
  
<script>
export default {
name: 'Navbar2',
}
</script>

<style scoped>
.flex-container {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
  padding-left: 5px;
  padding-right: 15px;
  background: rgb(255,255,255);
/* background: linear-gradient(90deg, rgba(255,255,255,1) 4%, rgba(29,184,253,1) 61%, rgba(252,176,69,1) 100%); */
  height: 40px;
  box-shadow: 2px 2px 3px 0px rgba(0, 0, 0, 0.185);
  font-family: system-ui;
  font-weight: 500;
}

.flex-item {
  display: flex;
  flex-direction: row;
}

.logo {
  width: 32px;
  height: auto;
}

.item-2 {
    padding-left: 15px;
    gap: 15px;
}

.nav-links {
    color:rgb(0, 0, 0);
}

.nav-links:hover {
  color: rgba(0, 136, 169, 0.7);
}

.header_button {
  height: 25px;
  color: #f1efed;
  width: 60px;
  margin-bottom: 0;
  background-color: rgba(0, 136, 169, 1);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease 0s;
}

.header_button:hover {
  background-color: rgba(0, 136, 169, 0.7);
}

</style>
  