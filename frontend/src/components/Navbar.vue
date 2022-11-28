<template>
  
  <header class="header">
    <img class="logo" src="@/assets/logo-no-background.png" alt="logo" />
    <nav>
      <ul class="nav__links">
        <li><a class="#" href="#">Home</a></li>
        <li>
          <router-link :to="{name: 'datatable'}" exact>Datatable</router-link>
        </li>
        <li>
          <router-link :to="{name: 'datatablequasar'}" exact>DatatableQuasar</router-link>
        </li>
        <li>
          <router-link :to="{name: 'login'}" exact
            ><button class="header_button">Login</button></router-link
          >
        </li>
      </ul>
    </nav>
  </header>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3"></div>
      <div class="collapse navbar-collapse" id="navbarSupportContent"></div>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link :to="{name: 'datatable'}" exact>DataTable</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped>
header {
  display: flex;
  width: 100%;
  height: 40px;
  justify-content: flex-end;
  background-color: #24252a;
  align-items: center;
  padding: 0px 20px 0px 20px;
  position: fixed;
  top: 0;
  z-index: 100;
}

.logo {
  margin-right: auto;
  width: 90px;
  height: auto;
  cursor: pointer;
}

header li,
header a {
  display: inline-block;
  padding: 8px;
  font-weight: 500;
  font-size: 14px;
  align-items: center;
  color: #edf0f1;
  text-decoration: none;
  cursor: pointer;
}

header ul {
  margin: 0;
  padding: 0px;
  list-style: none;
}

.nav__links {
  list-style: none;
}

.nav__links li {
  display: inline-block;
  /* padding: 0px 20px; */
  align-items: center;
  /* margin-top: 15px; */
}

.nav__links li a {
  transition: all 0.3s ease 0s;
}

.nav__links a:hover {
  color: rgba(0, 136, 169, 1);
}

header li:hover {
  color: rgba(0, 136, 169, 1);
}

.header a .header_button {
  height: 25px;
  color: #edf0f1;
  width: 60px;
  margin-bottom: 0;
  background-color: rgba(0, 136, 169, 1);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease 0s;
}

.header button:hover {
  background-color: rgba(0, 136, 169, 0.7);
}

.cta button {
  align-items: center;
}
</style>
