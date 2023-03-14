<template>
  <div id="app">
    <div class="row">
      <div class="col-md-1">
        <img src="./assets/HIT.png" alt="HIT" style="height: 100px; margin-left: 10px; margin-top: 10px;padding: 0px">
      </div>
      <div class="col-md-11" style="border-bottom: 2px black">
        <div class="page-header">
          <router-link to="/" style="text-decoration: none">
            <h1 style="padding-top: 30px">RPKI Data Analysis System</h1>
          </router-link>
<!--          <router-view></router-view>-->
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3" style="background-color: darkgray;padding-bottom: 950px">
        <ul id="sidebarMenu">
          <div class="btn-group" style="font-size: 20px;align-items: center;margin-top: 50px">Overview:
              <button type="button" class="btn btn-info dropdown-toggle btn-lg" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="margin-top: 20px;margin-bottom: 20px;margin-left: 65px;padding-left: 45px;padding-right: 45px">
                Repository <span class="caret"></span>
              </button>
              <ul class="dropdown-menu" style="font-size: 25px;">
                <li>
                  <router-link to="/Ripe" style="text-decoration: none;color: black;">
                    Ripe
                  </router-link>
                </li>
                <li>
                  <router-link to="/Ripe" style="text-decoration: none;color: black">
                    Arin
                  </router-link>
                </li>
                <li>
                  <router-link to="/Ripe" style="text-decoration: none;color: black">
                    Afrinic
                  </router-link>
                </li>
                <li>
                  <router-link to="/Ripe" style="text-decoration: none;color: black">
                    Apnic
                  </router-link>
                </li>
                <li>
                  <router-link to="/Ripe" style="text-decoration: none;color: black">
                    Lacnic
                  </router-link>
                </li>
              </ul>
            </div>
          <div class="btn-group" style="font-size: 20px;align-items: center;text-align: center;margin-top: 30px">Authentication Link:
              <button type="button" class="btn btn-info dropdown-toggle btn-lg" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="margin-top: 20px;margin-bottom: 20px;margin-left:20px;padding-left: 45px;padding-right: 45px">
                Repository <span class="caret"></span>
              </button>
              <ul class="dropdown-menu" style="font-size: 25px;">
                <li>
                  <router-link to="/RipeAuthT" style="text-decoration: none;color: black">
                    Ripe
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuthT" style="text-decoration: none;color: black">
                    Arin
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuthT" style="text-decoration: none;color: black">
                    Afrinic
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuthT" style="text-decoration: none;color: black">
                    Apnic
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuthT" style="text-decoration: none;color: black">
                    Lacnic
                  </router-link>
                </li>
              </ul>
            </div>
          <div class="btn-group" style="font-size: 20px;align-items: center;text-align: center;margin-top: 30px">Authentication Links:
              <button type="button" class="btn btn-info dropdown-toggle btn-lg" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="margin-top: 20px;margin-bottom: 20px;margin-left:20px;padding-left: 45px;padding-right: 45px">
                Repository <span class="caret"></span>
              </button>
              <ul class="dropdown-menu" style="font-size: 25px;">
                <li>
                  <router-link to="/RipeAuth" style="text-decoration: none;color: black">
                    Ripe
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuth" style="text-decoration: none;color: black">
                    Arin
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuth" style="text-decoration: none;color: black">
                    Afrinic
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuth" style="text-decoration: none;color: black">
                    Apnic
                  </router-link>
                </li>
                <li>
                  <router-link to="/RipeAuth" style="text-decoration: none;color: black">
                    Lacnic
                  </router-link>
                </li>
              </ul>
            </div>
          <div style="font-size: 20px;margin-top: 20px;align-items: center;">Route Origin Validation:
            <button type="button" class="btn btn-info" style="font-size: 20px;margin-top: 20px;margin-bottom: 20px;margin-left:155px;padding-left: 83px;padding-right: 82px;padding-top: 8px;padding-bottom: 8px">
              <router-link to="/Rov" style="text-decoration: none;color: white">
                ROV
              </router-link>
            </button>
          </div>
        </ul>
      </div>
      <div class="col-md-9">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
// import HelloWorld from './components/HelloWorld'
// import Ripe from './components/Ripe'
export default {
  name: 'App'
}
</script>

<style>

</style>
