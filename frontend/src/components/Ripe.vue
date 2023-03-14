<template>
  <div>
    <div class="btn-group" style="margin-left:0px;margin-right: 50px;margin-top: 10px;margin-bottom: 20px;padding: 10px">
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
        <button type="submit" class="btn btn-default" onclick="search()">Search</button>
      </form>
    </div>
    <div class="row" style="font-size: 20px;">
      <p style="margin-left: 20px;margin-bottom: 0px;height: 30px;margin-top: 10px">The number of ASs:</p><div class="col-md-1" id="asn_num" style="font-size: 30px;margin-left: 0px;">unknown</div>
      <p style="margin-bottom: 0px;height: 30px;margin-top: 10px">The number of IP blocks:</p><div class="col-md-1" id="ip_num" style="font-size: 30px;margin-left: 0px">unknown</div>
      <p style="margin-bottom: 0px;height: 30px;margin-top: 10px">The number of Certificates:</p><div class="col-md-1" id="cert_num" style="font-size: 30px;margin-left: 0px">unknown</div>
      <p style="margin-bottom: 0px;height: 30px;margin-top: 10px">The number of ROAs:</p><div class="col-md-1" id="roa_num" style="font-size: 30px;margin-left: 0px">unknown</div>
    </div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th>ASN</th>
        <th>IP Block</th>
        <th>Max Length</th>
        <th>Not Before</th>
        <th>Not After</th>
      </tr>
      </thead>
      <tbody id="table_body">
      <tr>
        <td id="asn"></td>
        <td id="ip_block"><a onclick="show_certificate('')"></a></td>
        <td id="maxlength"></td>
        <td id="notbefore"></td>
        <td id="notafter"></td>
      </tr>
      <h1></h1>
      </tbody>
    </table>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
export default {
  name: 'Ripe',
  mounted () {
    // let self = this;
    const _this = this
    window.show_certificate = function (ippre) {
      _this.show_cert(ippre)
    }
    window.cleantext = function (ippre) {
      _this.cleantext1(ippre)
    }
    window.search = function () {
      _this.search2()
    }
  },
  methods: {
    overview: function (date) {
      this.$http.get('http://172.20.43.10:8000/api/show_data', {params: {Date: date, Repo: 'Ripencc', repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          document.getElementById('asn_num').innerHTML = res['asn_number']
          document.getElementById('ip_num').innerHTML = res['ip_block_number']
          document.getElementById('cert_num').innerHTML = res['cert_num']
          document.getElementById('roa_num').innerHTML = res['roa_num']
          // console.log(res['list'][0].fields['asn'])
          var html = ''
          for (var i = 0; i < 50; i++) {
            html = html + '<tr><td><a type="button" onclick="cleantext(\'' + res['list'][i].fields['ip_pre'] + '\')">' + res['list'][i].fields['asn'] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_certificate(\'' + res['list'][i].fields['ip_pre'] + '\')">' + res['list'][i].fields['ip_pre'] + '</a></td>' +
              '<td>' + res['list'][i].fields['max_len'] + '</td>' +
              '<td>' + res['list'][i].fields['not_before'] + '</td>' +
              '<td>' + res['list'][i].fields['not_after'] + '</td>'
            html = html + '</tr><h1 style="font-size: 20px" id="' + res['list'][i].fields['ip_pre'] + '"></h1><h1 style="font-size: 20px" id="roa' + res['list'][i].fields['ip_pre'] + '"></h1>'
          }
          document.getElementById('table_body').innerHTML = html
          document.getElementById('datetm').innerHTML = date
        })
    },
    show_cert: function (ippre) {
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/show_cert', {params: {ipb: ippre, Date: date, Repo: 'Ripencc', repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          document.getElementById('roa' + ippre + '').innerText = res['roa']
          document.getElementById('' + ippre + '').innerText = res['cert']
        })
    },
    cleantext1: function (ippre) {
      document.getElementById('' + ippre + '').innerText = ''
      document.getElementById('roa' + ippre + '').innerText = ''
    },
    search2: function () {
      var ippre = this.$refs.getValue.value
      var date = document.getElementById('datetm').innerText
      document.getElementById('table_body').innerHTML = ''
      this.$http.get('http://172.20.43.10:8000/api/search', {params: {Date: date, Repo: 'Ripencc', IP_block: ippre}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          var html = '<tr><td><a type="button" onclick="cleantext(\'' + res['list'][1] + '\')">' + res['list'][0] + '</a></td>' +
              '<td><a class="ref" type="button" onclick="show_certificate(\'' + res['list'][1] + '\')">' + res['list'][1] + '</a></td>' +
              '<td>' + res['list'][2] + '</td>' +
              '<td>' + res['list'][3] + '</td>' +
              '<td>' + res['list'][4] + '</td>'
          html = html + '</tr><h1 style="font-size: 20px" id="' + res['list'][1] + '"></h1><h1 style="font-size: 20px" id="roa' + res['list'][1] + '"></h1>'
          document.getElementById('table_body').innerHTML = html
        })
    }
  }
}
</script>

<style scoped>

</style>
