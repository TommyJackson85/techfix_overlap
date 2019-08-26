//Charts page
//https://stackoverflow.com/questions/44396737/how-to-shorten-chart-js-label
//https://jsfiddle.net/6bexkyd9/
/*var progress_options = {
    maintainAspectRatio: false
};*/
var options = {
        maintainAspectRatio: false,
        legend: {
            labels: {
                generateLabels: function(chart){
                    var data = chart.data;
                    if (data.labels.length && data.datasets.length) {
                        return data.labels.map(function(label, i) {
                            var meta = chart.getDatasetMeta(0);
                            var ds = data.datasets[0];
                            var arc = meta.data[i];
                            var custom = arc && arc.custom || {};
                            var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                            var arcOpts = chart.options.elements.arc;
                            var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                            var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                            var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);
                            var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];
                            if (label.length > 17) {
                                return {
                                    text: label.substr(0, 17) + ' ...' + ' ('+ value + ')',
                                    fillStyle: fill,
                                    strokeStyle: stroke,
                                    lineWidth: bw,
                                    hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                    index: i
                                } //truncate
                            } else {
                                return {
                                    text: label + ' ('+ value + ')',
                                    fillStyle: fill,
                                    strokeStyle: stroke,
                                    lineWidth: bw,
                                    hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                    index: i
                                }
                            }
                        })
                    }
                }
            }
        }
    }
//Chart.defaults.global.elements.rectangle


//doughnut chart
var ctx = function(id) { 
    return document.getElementById(id).getContext('2d'); 
}

var ctxDaily = ctx('dailyProgressChart');
var ctxWeekly = ctx('weeklyProgressChart');
var ctxMonthly = ctx('monthlyProgressChart');

var daily_progress_chart = new Chart(ctxDaily, {
    type: 'doughnut',
    data: daily_data,
    options: options
});
var weekly_progress_chart = new Chart(ctxWeekly, {
    type: 'doughnut',
    data: weekly_data,
    options: options
});
var monthly_progress_chart = new Chart(ctxMonthly, {
    type: 'doughnut',
    data: monthly_data,
    options: options
});


$('#monthly_graph').show();
$('#weekly_graph').hide();
$('#monthly_graph').hide();

/* 

$("#bugs_graph_toggle").click(function(){
    $("#vote_graphs").fadeOut( "slow", function(){
            $("#feature_votes_graph").hide();
            $("#bug_votes_graph").show();
    });
    $("#vote_graphs").fadeIn( "slow" );
});
*/


$("#monthly_graph_toggle").click(function () {
    $("#average_graphs").fadeOut( "slow", function(){
        $("#monthly_graph").show();
        $("#weekly_graph").hide();
        $("#daily_graph").hide();
    });
    
    $('#monthly_graph_toggle').attr("disabled", true);
    $("#weekly_graph_toggle").attr("disabled", false);
    $("#daily_graph_toggle").attr("disabled", false);

    $('#monthly_graph_toggle').addClass('activated_button');
    $("#weekly_graph_toggle").removeClass('activated_button');
    $("#daily_graph_toggle").removeClass('activated_button');    
    
    $("#average_graphs").fadeIn("slow");
});

$("#weekly_graph_toggle").click(function () {
    $("#average_graphs").fadeOut( "slow", function(){
        $("#weekly_graph").show();
        $("#monthly_graph").hide();
        $("#daily_graph").hide();
    });
    
    $('#weekly_graph_toggle').attr("disabled", true);
    $("#monthly_graph_toggle").attr("disabled", false);
    $("#daily_graph_toggle").attr("disabled", false);
    
    $('#weekly_graph_toggle').addClass('activated_button');
    $("#monthly_graph_toggle").removeClass('activated_button');
    $("#daily_graph_toggle").removeClass('activated_button');
    
    
    $("#average_graphs").fadeIn("slow");
});

$('#daily_graph_toggle').click(function(){
    $("#average_graphs").fadeOut( "slow", function(){
        $("#daily_graph").show();
        $("#monthly_graph").hide();
        $("#weekly_graph").hide();
    });
    
    $('#daily_graph_toggle').attr("disabled", true);
    $("#weekly_graph_toggle").attr("disabled", false);
    $("#monthly_graph_toggle").attr("disabled", false);
    
    $('#daily_graph_toggle').addClass('activated_button');
    $("#weekly_graph_toggle").removeClass('activated_button');
    $("#monthly_graph_toggle").removeClass('activated_button');
    
    
    $("#average_graphs").fadeIn("slow");
})
$('#daily_graph_toggle').attr("disabled", true);

var ctxBugVotes = ctx('higestBugsVotedChart');
var ctxFeatureVotes = ctx('higestFeaturesVotedChart');

var most_voted_bugs = new Chart(ctxBugVotes, {
    type: 'doughnut',
    data: bug_votes_data,
    options: options,
});

var most_voted_features = new Chart(ctxFeatureVotes, {
    type: 'doughnut',
    data: feature_votes_data,
    options: options,
});

$("#bug_votes_graph").show();
$("#feature_votes_graph").hide();

$("#bugs_graph_toggle").click(function(){
    $("#vote_graphs").fadeOut( "slow", function(){
            $("#feature_votes_graph").hide();
            $("#bug_votes_graph").show();
    });
    
    $("#features_graph_toggle").attr("disabled", false);
    $("#bugs_graph_toggle").attr("disabled", true);
    
    $("#features_graph_toggle").removeClass('activated_button');
    $("#bugs_graph_toggle").addClass('activated_button');
    
    $("#vote_graphs").fadeIn( "slow" );
});
$('#bugs_graph_toggle').attr("disabled", true);

$('#features_graph_toggle').click(function(){
    
    $("#vote_graphs").fadeOut( "slow", function(){
        $("#bug_votes_graph").hide();
        $("#feature_votes_graph").show();        
    });
    
    $("#bugs_graph_toggle").attr("disabled", false);
    $("#features_graph_toggle").attr("disabled", true);
    
    $("#bugs_graph_toggle").removeClass('activated_button');
    $("#features_graph_toggle").addClass('activated_button');
    
    $("#vote_graphs").fadeIn( "slow" );
})

