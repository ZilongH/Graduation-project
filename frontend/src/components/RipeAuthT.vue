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
        <button type="submit" class="btn btn-default" onclick="searchT()">Search</button>
      </form>
    </div>
  <table class="table table-hover" style="align-items: center;text-align: center">
      <thead>
      <tr>
        <th><a type="button" v-on:click="clean_content()">Object</a></th>
      </tr>
      </thead>
      <tbody id="table_body">
      <tr style="color: #42b983">
        <td><a onclick="show_content('')"></a></td>
      </tr>
      </tbody>
  </table>
</div>
</template>

<script>
export default {
  name: 'RipeAuthT',
  mounted () {
    // let self = this;
    const _this = this
    window.searchT = function () {
      _this.search4()
    }
    window.show_content = function (uri) {
      _this.show_content1(uri)
    }
    // window.clean_content = function () {
    //   _this.cleantext3()
    // }
  },
  methods: {
    overview: function (date) {
      document.getElementById('datetm').innerHTML = date
    },
    search4: function () {
      var ippre = this.$refs.getValue.value
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/show_link', {params: {Date: date, IP_block: ippre, Repo: 'Ripe'}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // console.log(res['list'])
          var html = ''
          for (var i = 4; i >= 0; i--) {
            html = html + '<tr><td><a id="' + i + '" type="button" onclick="show_content(\'' + res['list'][i] + '\')">' + res['list'][i] + '</a></td></tr><h1 name="content" style="font-size: 20px;text-align: left" id="' + res['list'][i] + '"></h1>'
          }
          html = html + '<tr><td>AS' + res['asn'] + ' ' + ippre + '</td></tr>'
          document.getElementById('table_body').innerHTML = html
        })
    },
    show_content1: function (uri) {
      var date = document.getElementById('datetm').innerText
      this.$http.get('http://172.20.43.10:8000/api/show_content', {params: {Date: date, Repo: 'Ripe', URI: uri}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // console.log(res)
          document.getElementById(uri).innerText = res['content']
        })
    },
    clean_content: function () {
      for (var i = 0; i < 5; i++) {
        var id = document.getElementById('' + i + '').innerText
        if (id !== '') {
          document.getElementById('' + id + '').innerText = ''
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
