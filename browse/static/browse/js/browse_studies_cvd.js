

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
