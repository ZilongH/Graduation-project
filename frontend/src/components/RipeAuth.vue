<template>
  <div>
    <div class="btn-group" style="margin-left:0px;margin-right: 50px;margin-top: 10px;margin-bottom: 0px;padding: 10px">
      <button type="button" class="btn btn-default btn-lg dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding-top: 10px;padding-bottom: 10px;padding-left: 20px;padding-right: 30px">
        Date  <span class="caret"></span>
      </button>
      <ul class="dropdown-menu">
        <li><a type="button" v-on:click="overview('2022-05-22')">2022-05-22</a></li>
        <li><a type="button" v-on:click="overview('2022-05-23')">2022-05-23</a></li>
        <li><a type="button" v-on:click="overview('2022-05-24')">2022-05-24</a></li>
        <li><a type="button" v-on:click="overview('2022-05-25')">2022-05-25</a></li>
        <li><a type="button" v-on:click="overview('2022-05-26')">2022-05-26</a></li>
        <li><a type="button" v-on:click="overview('2022-05-27')">2022-05-27</a></li>
        <li><a type="button" v-on:click="overview('2022-05-28')">2022-05-28</a></li>
        <li><a type="button" v-on:click="overview('2022-05-29')">2022-05-29</a></li>
        <li><a type="button" v-on:click="overview('2022-05-30')">2022-05-30</a></li>
        <li><a type="button" v-on:click="overview('2022-05-31')">2022-05-31</a></li>
        <li><a type="button" v-on:click="overview('2022-06-01')">2022-06-01</a></li>
      </ul>
      <p id="datetm" style="font-size: 30px;margin-bottom: 0px;margin-left: 10px"></p>
      <form style="margin-left: 20px" class="form-inline">
        <div class="form-group">
          <label for="exampleInput">IP Block: </label>
          <input type="text" class="form-control" id="exampleInput" placeholder="XXX.XXX.XXX.XXX/XX" ref="getValue">
        </div>
        <button type="submit" class="btn btn-default" onclick="searchA()">Search</button>
      </form>
    </div>
    <table class="table table-hover">
      <tbody>
      <tr>
        <h3 id="rout_head">Routinator Message:</h3>
        <h5 id="routinator">Unknown</h5>
      </tr>
      </tbody>
    </table>
    <table class="table table-hover">
      <thead>
      <tr>
        <th>ASN</th>
        <th>IP Block</th>
        <th>ROA URI</th>
        <th>Certificate URI</th>
      </tr>
      </thead>
      <tbody id="table_body">
      <tr>
        <td id="asn"></td>
        <td id="ip_block"><a onclick="show_roa('')"></a></td>
        <td id="roa_uri"><a onclick="show_cert1('', '')"></a></td>
        <td id="cert_uri"><a onclick="show_auth('', '')"></a></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'RipeAuth',
  mounted () {
    // let self = this;
    const _this = this
    window.show_roa = function (ippre) {
      _this.show_roa1(ippre)
    }
    window.show_cert1 = function (roauri, ippre) {
      _this.show_cert2(roauri, ippre)
    }
    window.show_auth = function (certuri, ippre) {
      _this.show_auth1(certuri, ippre)
    }
    window.cleantext = function (ippre) {
      _this.cleantext2(ippre)
    }
    window.searchA = function () {
      _this.search1()
    }
  },
  methods: {
    overview: function (date) {
      this.$http.get('http://172.20.43.10:8000/api/show_data_1', {params: {Date: date, Repo: 'Ripe', repo: 'ripencc'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // console.log(res['rout_len'])
          var routinator = ''
          for (var i = 0; i < res['rout_len']; i++) {
            routinator = routinator + res['routinator'][i] + '\n'
          }
          document.getElementById('routinator').innerText = routinator
          document.getElementById('datetm').innerHTML = date
          var html = ''
          for (var j = 0; j < 50; j++) {
            html = html + '<tr><td><a type="button" onclick="cleantext(\'' + res['list'][j][1] + '\')">AS' + res['list'][j][0] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_roa(\'' + res['list'][j][1] + '\')">' + res['list'][j][1] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_cert1(\'' + res['list'][j][2] + '\', \'' + res['list'][j][1] + '\')">' + res['list'][j][2] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_auth(\'' + res['list'][j][3] + '\', \'' + res['list'][j][1] + '\')">' + res['list'][j][3] + '</a></td>'
            html = html + '</tr><h1 style="font-size: 20px" id="' + res['list'][j][1] + '"></h1>'
          }
          document.getElementById('table_body').innerHTML = html
        })
    },
    show_roa1: function (ippre) {
      document.getElementById('' + ippre + '').innerText = ''
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/search_roa', {params: {Date: date, IP_block: ippre, Repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          document.getElementById('' + ippre + '').innerText = res['roa']
        })
    },
    show_cert2: function (roauri, ippre) {
      document.getElementById('' + ippre + '').innerText = ''
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/search_cert', {params: {Date: date, ROA_URI: roauri, Repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          document.getElementById('' + ippre + '').innerText = res['cert']
        })
    },
    show_auth1: function (certuri, ippre) {
      document.getElementById('' + ippre + '').innerText = ''
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/search_auth', {params: {Date: date, Cert_URI: certuri, Repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          document.getElementById('' + ippre + '').innerText = res['cert']
        })
    },
    cleantext2: function (ippre) {
      document.getElementById('' + ippre + '').innerText = ''
    },
    search1: function () {
      var ippre = this.$refs.getValue.value
      var date = document.getElementById('datetm').innerText
      document.getElementById('rout_head').innerHTML = ''
      document.getElementById('routinator').innerHTML = ''
      document.getElementById('table_body').innerHTML = ''
      this.$http.get('http://172.20.43.10:8000/api/search_1', {params: {Date: date, Repo: 'Ripe', IP_block: ippre}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          var html = '<tr><td><a type="button" onclick="cleantext(\'' + res['list'][1] + '\')">AS' + res['list'][0] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_roa(\'' + res['list'][1] + '\')">' + res['list'][1] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_cert1(\'' + res['list'][2] + '\', \'' + res['list'][1] + '\')">' + res['list'][2] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_auth(\'' + res['list'][3] + '\', \'' + res['list'][1] + '\')">' + res['list'][3] + '</a></td>'
          html = html + '</tr><h1 style="font-size: 20px" id="' + res['list'][1] + '"></h1>'
          // html = html + '</tr><h1 style="font-size: 20px" id="' + res['list'][1] + '"></h1><h1 style="font-size: 20px" id="roa' + res['list'][1] + '"></h1>'
          document.getElementById('table_body').innerHTML = html
        })
    }
  }
}
</script>

<style scoped>

</style>
