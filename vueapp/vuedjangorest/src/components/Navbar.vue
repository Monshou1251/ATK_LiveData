<template>
    <header class="header">
      <!-- <img
        class="logo"
        src="../../static/png/logo-no-background.png"
        alt="logo"
      /> -->
      <nav>
        <ul class="nav__links">
          <li>Home</li>
          <li>Contacts</li>
          <li>FAQ</li>
        </ul>
      </nav>
      <a class="#" href="#"><button class="header_button">Login</button></a>
    </header>
    <div class="nav-bar">
        <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
            <div class="container mw-0 px-3">
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportContent"></div>
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <router-link :to = "{name: 'datatable'}" exact>DataTable</router-link>
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
    a {
        color:#000;
    }

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

    .nav__links {
        list-style: none;
    }

    .nav__links li {
        display: inline-block;
        /* padding: 0px 20px; */
    }

    .nav__links li a {
        transition: all 0.3s ease 0s;
    }
</style>