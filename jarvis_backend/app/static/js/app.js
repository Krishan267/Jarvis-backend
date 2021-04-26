
/**
 * function to get all the historical trade data for the logged in user
 */

function getTradeData() {
    var username = document.getElementById('username').textContent;
    $.ajax({
        url:'trade_data/'+username,
        type:'GET',
        success: function(result){
            var rows = result.data
            var html = "";
            for (var i = 0; i < Object.values(rows)[0].length; i++) {
                console.log("1")
                html+="<tr class='td-data'>";
                html+="<td>"+rows.exchange[i]+"</td>";
                html+="<td>"+rows.symbol[i]+"</td>";
                html+="<td>"+rows.entry_time[i]+"</td>";
                html+="<td>"+rows.entry_price[i]+"</td>";
                html+="<td>"+rows.qty[i]+"</td>";
                html+="<td>"+rows.exit_time[i]+"</td>";
                html+="<td>"+rows.exit_price[i]+"</td>";
                html+="<td>"+rows.net_pnl_usd[i]+"</td>";
                html+="<td>"+rows.net_pnl_percent[i]+"</td>";
                html+="<td>"+rows.result[i]+"</td>";
                html+="</tr>";
    
            }
            document.getElementById("trade-data").innerHTML = html;
        },
        error: function(error) {
            console.log('ERROR ${error}')
        }
      });
}

$( "#trade_download" ).click(function() {
    var username = document.getElementById('username').textContent;
    $.ajax({
        url:'trade_data_download/'+username,
        type:'GET',
        success: function(result){
            window.location='trade_data_download/'+username

            
        }
    });
  });

  $( "#pos_download" ).click(function() {
    var username = document.getElementById('username').textContent;
    $.ajax({
        url:'open_positions_download/'+username,
        type:'GET',
        success: function(result){
            window.location='open_positions_download/'+username

            
        }
    });
  });


function getOpenPositions() {
    var username = document.getElementById('username').textContent;
    
    $.ajax({
        url:'open_positions/'+username,
        type:'GET',
        success: function(result){
            var rows = result.data
            var html = "";
            for (var i = 0; i < Object.values(rows)[0].length; i++) {
                console.log("1")
                html+="<tr class='td-data'>";
                html+="<td>"+rows.exchange[i]+"</td>";
                html+="<td>"+rows.symbol[i]+"</td>";
                html+="<td>"+rows.entry_time_utc[i]+"</td>";
                html+="<td>"+rows.price[i]+"</td>";
                html+="<td>"+rows.side[i]+"</td>";
                html+="<td>"+rows.open_pos[i]+"</td>";
                html+="<td>"+rows.dollar_qty[i]+"</td>";
                // html+="<td>"+rows.net_pnl_usd[i]+"</td>";
                // html+="<td>"+rows.net_pnl_percent[i]+"</td>";
                // html+="<td>"+rows.result[i]+"</td>";
                html+="</tr>";
    
            }

            console.log(html);
    
            document.getElementById("position-data").innerHTML = html;
        },
        error: function(error) {
            console.log('ERROR ${error}')
        }
      });
}

/**
 * function to get all the strategies services for the user
 */
function startService(id) {
    console.log('here in start service')
    var username = document.getElementById('username').textContent;
    console.log(id); 
    $.ajax({
        url:'start_strategy/'+username+"/"+id,
        type:'GET',
        success: function(result){ 
            
            console.log(result)
        }
    });
    // $('.change-status-stopped').html("<em class='fa fa-circle' style='color: green; font-size: 10px'></em>"+'Start');
    // $('.change-button-color-green').html("<button class='btn btn-secondary start_btn' onclick='stopService()'>"+"Start"+"</button>");
}

function stopService(id) {
    console.log('here in stop service')
    var username = document.getElementById('username').textContent;
    console.log(id); 
    $.ajax({
        url:'stop_strategy/'+username+"/"+id,
        type:'GET',
        success: function(result){ 
            
            console.log(result)
        }
    });
    // manageStrategy();
    // $('.change-status-on').html("<em class='fa fa-circle' style='color: red; font-size: 10px'></em>"+'Stop');
    // $('.change-button-color-red').html("<button class='btn btn-secondary stop_btn' onclick='startService()'>"+"Stop"+"</button>");
}

function manageStrategy() {
    var username = document.getElementById('username').textContent;
    try {
    $.ajax({
        url:'strategies/'+username,
        type:'GET',
        success: function(result){
            var strategies_data = result.data
            console.log(strategies_data)
            var html = "";
            if (jQuery.isEmptyObject(strategies_data)== false){
            for (var i = 0; i < Object.values(strategies_data)[0].length; i++) {
                html+="<tr>";
                html+="<td>"+strategies_data.strategy[i]+"</td>";
                if (strategies_data.status[i] === 'RUNNING'){
                    html+="<td  class='change-status-on'><em class='fa fa-circle' style='color: green; font-size: 10px'></em>"+strategies_data.status[i]+"</td>"
                    html+="<td class='text-right change-button-color-red'>"
                    html+="<button id= '"+strategies_data.strategy[i]+"'class='btn btn-secondary stop_btn' onclick='stopService(this.id)'>Stop</button>"
                    html+="</td>"
                }
                else if(strategies_data.status[i] === 'STOPPED'){
                    html+="<td class='change-status-stopped'><em class='fa fa-circle' style='color: red; font-size: 10px'></em>"+strategies_data.status[i]+"</td>"
                    html+="<td class='text-right change-button-color-green'>"
                    html+="<button id= '"+strategies_data.strategy[i]+"'class='btn btn-secondary start_btn' onclick='startService(this.id)'>Start</button>"
                    html+="</td>"
                }
                else{
                    html+="<td class='change-status-starting'><em class='fa fa-circle' style='color: red; font-size: 10px'></em>"+strategies_data.status[i]+"</td>"
                    html+="<td class='text-right change-button-color-green'>"
                    // html+="<button class='btn btn-secondary start_btn' onclick='startService()'></button>"
                    html+="</td>"
                }
                html+="</tr>";
            }
            document.getElementById("strategy").innerHTML = html;
        }else{
            console.log("empty")
        }
        },
        error: function(error) {
            console.log('ERROR ${error}')
        }
      });
    }
    catch(err) {
console.log("error");

    }
}

/**
 * function to get the bar related data and make chart
 */

function makebarData() {
    $.ajax({
        url:'bar_data',
        type:'GET',
        success: function(data){
            var margin = {top: 30, right: 30, bottom: 80, left: 60},
            width = 1060 - margin.left - margin.right,
            height = 350 - margin.top - margin.bottom;
            max_value = data.max_val
            data=data.bar_data
            // append the svg object to the body of the page
            var svg = d3.select("#my_dataviz")
                .append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");


            // X axis
            var x = d3.scaleBand()
                .range([ 0, width ])
                .domain(data.map(function(d) { return d.entry_time; }))
                .padding(0.2);
                svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x))
                .selectAll("text")
                    .attr("transform", "translate(-10,0)rotate(-45)")
                    .style("text-anchor", "end");

            // Add Y axis
            var y = d3.scaleLinear()
                .domain([0, max_value])
                .range([ height, 0]);
                svg.append("g")
                .call(d3.axisLeft(y));

            // Bars
            svg.selectAll("mybar")
            .data(data)
            .enter()
            .append("rect")
                .attr("x", function(d) { return x(d.entry_time); })
                .attr("y", function(d) { return y(d.entry_qty); })
                .attr("width", x.bandwidth())
                .attr("height", function(d) { return height - y(d.entry_qty); })
                .attr("fill", "#69b3a2")
        },
        error: function(error) {
            console.log('ERROR ${error}')
        }
    });

}

/**
 * funtion to get protfolio data and make a line chart
 */

function makeLineGraph() {
    $.ajax({
        url:'portfolio',
        type:'GET',
        success: function(result){

            var margin = {top: 10, right: 30, bottom: 30, left: 60},
            width = 1060 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;

            // append the svg object to the body of the page
            var svg = d3.select("#my_dataviz2")
                .append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");
            
            result.forEach(function(d) {
                // parseDate = d3.time.format("%Y-%m-%dT%H:%M:%SZ").parse
                d.entry_time = d3.timeParse("%Y-%m-%d")(d.entry_time);
                d.entry_qty = +d.entry_qty;
                });
            
            // console.log(result)

            var x = d3.scaleTime()
                .domain(d3.extent(result, function(d) { return d.entry_time; }))
                .range([ 0, width ]);
                svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            // Add Y axis
            var y = d3.scaleLinear()
                .domain([0, d3.max(result, function(d) { return +d.entry_qty; })])
                .range([ height, 0 ]);
                svg.append("g")
                .call(d3.axisLeft(y));
            

            // Add the line
            svg.append("path")
                .datum(result)
                .attr("fill", "none")
                .attr("stroke", "steelblue")
                .attr("stroke-width", 1.5)
                .attr("d", d3.line()
                .x(function(d) { return x(d.entry_time) })
                .y(function(d) { return y(d.entry_qty) })
                )

        },
        error: function(error) {
            console.log('ERROR ${error}')
        }
      });
}
getOpenPositions()
getTradeData()
manageStrategy()
makebarData()
makeLineGraph()

setInterval(function(){
    manageStrategy() // this will run after every 5 seconds
}, 5000);

/**
 <tr>
<td>Jassica</td>
<td><em class="fa fa-circle" style="color: green; font-size: 10px"></em> Start</td>
<td class="text-right">
<button class="btn btn-secondary start_btn">Start</button>
</td>
</tr>
<tr>
<td>Adam</td>
<td><em class="fa fa-circle" style="color: red; font-size: 10px"></em> Stop</td>
<td class="text-right">
<button class="btn btn-secondary stop_btn">Stop</button>
</td>
</tr>
 */