<template>
  <div>
    <div class="btn-group" style="margin-bottom: 10px">
      <button type="submit" class="btn btn-default" onclick="show()">Show</button>
      <p></p>
      <form style="margin-left: 20px" class="form-inline">
        <div class="form-group">
          <label for="exampleInput">IP Block:  </label>
          <input type="text" class="form-control" id="exampleInput" placeholder="XXX.XXX.XXX.XXX/XX" ref="getValue">
        </div>
        <button type="submit" class="btn btn-default" onclick="searchR()">Search</button>
      </form>
    </div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th>ASN</th>
        <th>IP Block</th>
        <th>Version</th>
        <th>Result</th>
        <th>Reason</th>
        <th>First Time</th>
        <th>Last Time</th>
      </tr>
      </thead>
      <tbody id="table_body">
      <tr style="color: #42b983">
        <td id="asn"></td>
        <td id="ip_Block"></td>
        <td id="Version"></td>
        <td id="Result"></td>
        <td id="Reason"></td>
        <td id="FirstTime"></td>
        <td id="LastTime"></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Rov',
  mounted () {
    // let self = this;
    const _this = this
    window.searchR = function () {
      _this.search3()
    }
    window.show = function () {
      _this.show1()
    }
  },
  methods: {
    show1: function () {
      document.getElementById('table_body').innerHTML = ''
      this.$http.get('http://172.20.43.10:8000/api/show_rov')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // console.log(res)
          var html = ''
          for (var i = 0; i < 100; i++) {
            if (res['list'][i][3] === 'invalid') {
              html = html + '<tr style="background-color: darksalmon"><td>AS' + res['list'][i][1] + '</td>' +
              '<td>' + res['list'][i][0] + '</td>' +
              '<td>IPv' + res['list'][i][2] + '</td>' +
              '<td>' + res['list'][i][3] + '</td>' +
              '<td>' + res['list'][i][4] + '</td>' +
              '<td>' + res['list'][i][5] + '</td>' +
              '<td>' + res['list'][i][6] + '</td></tr>'
            } else if (res['list'][i][3] === 'not found') {
              html = html + '<tr style="background-color: khaki"><td>AS' + res['list'][i][1] + '</td>' +
              '<td>' + res['list'][i][0] + '</td>' +
              '<td>IPv' + res['list'][i][2] + '</td>' +
              '<td>' + res['list'][i][3] + '</td>' +
              '<td>' + res['list'][i][4] + '</td>' +
              '<td>' + res['list'][i][5] + '</td>' +
              '<td>' + res['list'][i][6] + '</td></tr>'
            } else {
              html = html + '<tr style="background-color: aquamarine"><td>AS' + res['list'][i][1] + '</td>' +
              '<td>' + res['list'][i][0] + '</td>' +
              '<td>IPv' + res['list'][i][2] + '</td>' +
              '<td>' + res['list'][i][3] + '</td>' +
              '<td>' + res['list'][i][4] + '</td>' +
              '<td>' + res['list'][i][5] + '</td>' +
              '<td>' + res['list'][i][6] + '</td></tr>'
            }
          }
          document.getElementById('table_body').innerHTML = html
        })
    },
    search3: function () {
      var ippre = this.$refs.getValue.value
      document.getElementById('table_body').innerHTML = ''
      this.$http.get('http://172.20.43.10:8000/api/search_rov', {params: {IP_block: ippre}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // console.log(res)
          var html = ''
          if (res['list'][3] === 'invalid') {
            html = '<tr style="background-color: darksalmon"><td>AS' + res['list'][0] + '</td>' +
            '<td>' + res['list'][1] + '</td>' +
            '<td>IPv' + res['list'][2] + '</td>' +
            '<td>' + res['list'][3] + '</td>' +
            '<td>' + res['list'][4] + '</td>' +
            '<td>' + res['list'][5] + '</td>' +
            '<td>' + res['list'][6] + '</td></tr>'
          } else if (res['list'][3] === 'not found') {
            html = '<tr style="background-color: khaki"><td>AS' + res['list'][0] + '</td>' +
            '<td>' + res['list'][1] + '</td>' +
            '<td>IPv' + res['list'][2] + '</td>' +
            '<td>' + res['list'][3] + '</td>' +
            '<td>' + res['list'][4] + '</td>' +
            '<td>' + res['list'][5] + '</td>' +
            '<td>' + res['list'][6] + '</td></tr>'
          } else {
            html = '<tr style="background-color: aquamarine"><td>AS' + res['list'][0] + '</td>' +
            '<td>' + res['list'][1] + '</td>' +
            '<td>IPv' + res['list'][2] + '</td>' +
            '<td>' + res['list'][3] + '</td>' +
            '<td>' + res['list'][4] + '</td>' +
            '<td>' + res['list'][5] + '</td>' +
            '<td>' + res['list'][6] + '</td></tr>'
          }
          document.getElementById('table_body').innerHTML = html
        })
    }
  }
}
</script>

<style scoped>

</style>
