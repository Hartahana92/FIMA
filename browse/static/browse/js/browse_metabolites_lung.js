///////////////////////////////Metabolite name///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex, searchData) {
        var met = $('#metabolite_name').val();



        if ( met.length === 0)
        {
            return true;
        }
        if (searchData[1].includes(met)) {
          return true;
        }
        return false;
    }
);
///////////////////////////////Super class///////////////////////////////
$.fn.dataTable.ext.search.push(
    function(  settings, data, dataIndex, searchData ) {
        var cl = $('#super_class').val();



        return true;
    }
);



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
  if (searchData[5].includes(el)) {
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

      if (stages.indexOf(searchData[6]) !== -1) {
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

      if (controls.indexOf(searchData[11]) !== -1) {
        return true;
      }

      return false;
    }
  );

  $("#checkAll_control").change(function(){
      $(".control").attr("checked", $(this).prop("checked"));
  });




//////////////////////////Specimen///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="specimen"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[3]) !== -1) {
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

      if (controls.indexOf(searchData[23]) !== -1) {
        return true;
      }

      return false;
    }
  );





//////////////////////////////////////////////////////////////IOn source///////////////////////////////
$.fn.dataTable.ext.search.push(
    function( settings, searchData, index, rowData, counter ) {

      var controls = $('input:checkbox[name="ion"]:checked').map(function() {
        return this.value.split('|');
      }).get();


      if (controls.length === 0) {
        return true;
      }

      if (controls.indexOf(searchData[24]) !== -1) {
        return true;
      }

      return false;
    }
  );



///////////////////////////////
var table = $('#met_table').DataTable({
      fixedColumns: {
        left: 2
    },

    pageLength : 7,
    lengthMenu: [[7, 10, 20, 50], [7, 10, 20, 50]],
    "bPaginate": true,
    "searching": false,
    "info":	true,
     "fixedHeader": true,
     "bFilter": true,
     "columnDefs": [
                {"className": "dt-center", "targets": "_all"},


                 {
                   // The `data` parameter refers to the data for the cell (defined by the
                     // `data` option, which defaults to the column being worked with, in
                     // this case `data: 0`.


                     //ref to hmdb
                     "render": function ( data, type, row ) {
                       if (data != "–"){

                         return '<a class="btn btn-outline-primary" target="_blank" href="' + "http://www.hmdb.ca/metabolites/" + data+'">' + data +"</a>";
                       }
                       else if (data == "–"){

                         return '<div class="btn btn-primary" >' + data + "</div>";
                       }
                     },
                     "targets": 0
                 },

                 /*meta page
                 {
  								"targets": 1,
                  "data": 0,
  								"render": function(data,type,full) {
                               if (data.length !== 1) {
                                        const chorus = '0';


                                        return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/HMDB" + chorus.repeat(11 - data.length) + data.substr(4) + '">' + full[1] +"</a>";
                                     }
                                else {
                                      return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[1] +"</a>";
                                }

  								},
                },*/
                {
                 "targets": 1,
                 "data": 0,
                 "render": function(data,type,full) {

                                     return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/" + data+'">' + full[1] +"</a>";
                              }

               },
                //pubmed
                {
                 "targets": 2,
                 "data": 2,
                 "render": function(data,type,full) {
                            return '<a target="_blank" target="_blank" href="' + "/browse_studies/PUBMED" + data+'">' + data +"</a>";
                 }
               },
                {
                 "targets": 14,
                 "data": 2,
                 "render": function(data,type,full) {
                            return '<a target="_blank" target="_blank" href="' + "/browse_metabolites/PUBMED" + data + "_mets" + '">' + full[14] +"</a>";
                 },
               },


                //средня концентрация контроль
                {
                "targets": 8,
                 "data": 8,
                 "render": function(data,type,full) {

                           var r = data.split("±");
                           if (r.length  > 1) {
                               let r1 = parseFloat(r[0].replace(',', '.')).toFixed(2);
                               let r2 = parseFloat(r[1].replace(',', '.')).toFixed(2);
                               return r1.toString() + "±" + r2.toString();
                         }
                           else {
                           return data;
                         }
                  }
              },

                //средн. конц контрольной
                {
                "targets": 10,
                 "data": 10,
                 "render": function(data,type,full) {

                           var r = data.split("±");
                           if (r.length  > 1) {
                               let r1 = parseFloat(r[0].replace(',', '.')).toFixed(2);
                               let r2 = parseFloat(r[1].replace(',', '.')).toFixed(2);
                               return r1.toString() + "±" + r2.toString();
                         }
                           else {
                           return data;
                         }
                  }
              },


                  //изменения
                  {
   								"targets": 9,
                   "data": 9,
                   "render": function(data,type,full) {
                             var r = parseFloat(data.replace(',', '.'))
                             if (!isNaN(r)) {
                               if(r > 0.01) {
    									                  return Number.parseFloat(r).toFixed(2);
                                }
                              else {
                                  if (r > 0.001){
                                      return "<0.01";
                                  }
                                  else {
                                      if (r > 0.0001) {
                                          return "<0.001";
                                      }
                                      else {
                                          return "<0.0001";
                                      }
                                  }
                              }
                            }
                            else {
                              return data;
                            }
    								}
                },
                  //p-val
                  {
   								"targets": 11,
                   "data": 11,
   								"render": function(data,type,full) {
                            var r = parseFloat(data.replace(',', '.'))
                            if (!isNaN(r)) {
                              if(r > 0.01) {
                                       return Number.parseFloat(r).toFixed(2);
                               }
                             else {
                                 if (r > 0.001){
                                     return "<0.01";
                                 }
                                 else {
                                     if (r > 0.0001) {
                                         return "<0.001";
                                     }
                                     else {
                                         return "<0.0001";
                                     }
                                 }
                             }
                           }
                           else {
                             return data;
                           }
                   }
  							},
                //fdr
                {
                "targets": 12,
                 "data": 12,
                "render": function(data,type,full) {
                          var r = parseFloat(data.replace(',', '.'))
                          if (!isNaN(r)) {
                            if(r > 0.01) {
                                     return Number.parseFloat(r).toFixed(2);
                             }
                           else {
                               if (r > 0.001){
                                   return "<0.01";
                               }
                               else {
                                   if (r > 0.0001) {
                                       return "<0.001";
                                   }
                                   else {
                                       return "<0.0001";
                                   }
                               }
                           }
                         }
                         else {
                           return data;
                         }
                 }
              },
              //vpr
              {
              "targets": 13,
               "data": 13,
              "render": function(data,type,full) {
                        var r = parseFloat(data.replace(',', '.'))
                        if (!isNaN(r)) {
                          if(r > 0.01) {
                                   return Number.parseFloat(r).toFixed(2);
                           }
                         else {
                             if (r > 0.001){
                                 return "<0.01";
                             }
                             else {
                                 if (r > 0.0001) {
                                     return "<0.001";
                                 }
                                 else {
                                     return "<0.0001";
                                 }
                             }
                         }
                       }
                       else {
                         return data;
                       }
               }

            },



            //stupid shit

            {
            "data": 7,
           "targets": 7,
           "render": function(data,type,full) {
                      return ('<a target="_blank" target="_blank" href="' + "/browse_metabolites/_" + full[0] + full[2].toString() + full[3] + '">' + data +"</a>").replace(',', '.'); // hmdb + pubmed + raw-p-val
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
table.columns( [15,16] ).visible( false );

$('input:checkbox').on('change', function () {
table.draw();
});


$('#metabolite_name').keyup( function() {
        table.draw();
    } );
$('#super_class').keyup( function() {
        table.draw();
    } );




} );
