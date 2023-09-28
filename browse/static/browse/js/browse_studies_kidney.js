
//////////////////////////CASES///////////////////////////////
$(document).ready( function () {
    $.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {
    var cases = $('input:checkbox[name="case"]:checked').map(function() {
      return this.value.split('|');
}).get();

if (cases.length === 0) {
  return true;
}

let found = false;
cases.forEach(function(el) {
  console.log(el)
  if (searchData[8].includes(el)) {
    found = true;
  }
});

return found;

}
);

$("#checkAll").change(function(){
    $(".case").attr("checked", $(this).prop("checked"));
});
///////////////////////////////Cancer stage///////////////////////////////

$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var stages = $('input:checkbox[name="cancer_stage"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (stages.length === 0) {
        return true;
      }

      if (stages.indexOf(searchData[9]) !== -1) {
        return true;
      }

      return false;
    }
  );

//////////////////////////Control///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="control"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[14]) !== -1) {
        return true;
      }

      return false;
    }
  );

  $("#checkAll_control").change(function(){
      $(".control").attr("checked", $(this).prop("checked"));
  });



///////////////////////////////Year of publication///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = parseInt( $('#y1').val());
        var max = parseInt( $('#y2').val());
        var year = data[2].split(' ').pop() || 0;

        if ( ( isNaN( min ) && isNaN( max ) ) ||
             ( isNaN( min ) && year <= max ) ||
             ( min <= year   && isNaN( max ) ) ||
             ( min <= year   && year <= max ) )
        {
            return true;
        }
        return false;
    }
);
//////////////////////////Specimen///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="specimen"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[6]) !== -1) {
        return true;
      }

      return false;
    }
  );

  $("#checkAll_specimen").change(function(){
      $(".specimen").attr("checked", $(this).prop("checked"));
  });



///////////////////////////////Chromatography///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="chromatography"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[19]) !== -1) {
        return true;
      }

      return false;
    }
  );





//////////////////////////////////////////////////////////////Chromatography///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="ion"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[20]) !== -1) {
        return true;
      }

      return false;
    }
  );


///////////////////////////////
var table = $('#paper_table').DataTable({
        fixedColumns: {
          left: 2
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true,
	  	//"searching": false,
	  	"info":	true,
	     "fixedHeader": true,
       "bFilter": true,
       "bProcessing": true,
        //"scrollX": true,

        "columnDefs": [
                    {"className": "dt-center", "targets": "_all"},
                    {


                        // The `data` parameter refers to the data for the cell (defined by the
                        // `data` option, which defaults to the column being worked with, in
                        // this case `data: 0`.


                        //ref to hmdb
                        "render": function ( data, type, row ) {
                          if (data != "–"){

                            return '<a class="btn btn-outline-primary" target="_blank" href="' + "https://pubmed.ncbi.nlm.nih.gov/" + data+'">' + data +"</a>";
                          }
                          else if (data == "–"){

                            return '<div class="btn btn-primary" >' + data + "</div>";
                          }
                        },
                        "targets": 0
                    },

                    //meta page
                    {
                    "targets": 1,
                     "data": 0,
                    "render": function(data,type,full) {
                               return '<a target="_blank" target="_blank" href="' + "/browse_studies/PUBMED" + data+'">' + full[1] +"</a>";
                    },
                   },
                   {
                   "targets": 4,
                    "data": 0,
                   "render": function(data,type,full) {
                              return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/PUBMED" + data + "_mets" + '">' + full[4] +"</a>";
                   },
                  },
                 ],
                 buttons: [
                       {
                               extend: 'print',
                               text: 'Print all',
                                 exportOptions: {
                                     modifier: {
                                       selected: null
                                 }
                             }
                         },
                     {
                         extend: 'print',
                         text: 'Print selected'
                     }
                 ],
                 select: true,

                 "dom": 'Brtlip'
});


$('input:checkbox').on('change', function () {
  table.draw();
});


$('#y1, #y2').keyup( function() {
        table.draw();
    } );

} );
