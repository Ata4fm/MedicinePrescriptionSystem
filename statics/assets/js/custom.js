new Vue({
    el: "#app",
    data: {
        search: "",
        random_lists: [],
        current_page: 1,
        total_pages: 0,
        next: null,
        previous: null,
        page_numbers: [],

    },
    beforeMount() {
        this.getData();
    },
    methods: {
        getData(url = "/dashboard/patients/api/patients/") {
            var self = this;
            if (self.search) {
                url += `?search=${self.search}`;
            }
            $.get(url)
                .done(function (response) {
                    self.random_lists = response.results;
                    self.next = response.next;
                    self.previous = response.previous;


                    const urlParams = new URLSearchParams(url.split('?')[1]);
                    self.current_page = urlParams.get('page') ? parseInt(urlParams.get('page')) : 1;

                    self.total_pages = Math.ceil(response.count / 10);
                    self.page_numbers = Array.from({length: self.total_pages}, (_, i) => i + 1);
                })
                .fail(function (error) {
                    console.error("خطا در دریافت داده", error)
                });
        },
        goToPage(page) {
            let url = `/dashboard/patients/api/patients/?page=${page}`;

            if (this.search) {
                url += `&`;
            }
            this.getData(url);
        },
        nextPage() {
            if (this.next) {
                this.getData(this.next);
            }
        },
        previousPage() {
            if (this.previous) {
                this.getData(this.previous);
            }
        }

    },
    watch: {
        "search": function () {
            this.getData();
        }
    }

})


new Vue({
    el: "#app2",
    data: {
        search: "",
        random_lists: [],
        current_page: 1,
        total_pages: 0,
        next: null,
        previous: null,
        page_numbers: []
    },
    beforeMount() {
        this.getData();
    },
    methods: {
        getData(url = "/dashboard/medicine/api/medicines/?") {
            var self = this;
            if (self.search) {
                url += `search=${self.search}`;
            }
            $.get(url)
                .done(function (response) {
                    self.random_lists = response.results;
                    self.next = response.next;
                    self.previous = response.previous;

                    const urlParams = new URLSearchParams(url.split('?')[1]);
                    self.current_page = urlParams.get('page') ? parseInt(urlParams.get('page')) : 1;

                    self.total_pages = Math.ceil(response.count / 10);
                    self.page_numbers = Array.from({length: self.total_pages}, (_, i) => i + 1);
                })
                .fail(function (error) {
                    console.error("خطا در دریافت داده", error)
                });
        },
        goToPage(page) {
            let url = `/dashboard/medicine/api/medicines/?page=${page}`;

            if (this.search) {
                url += `&`;
            }
            this.getData(url);
        },
        nextPage() {
            if (this.next) {
                this.getData(this.next);
            }
        },
        previousPage() {
            if (this.previous) {
                this.getData(this.previous);
            }
        }

    },
    watch: {
        "search": function () {
            this.getData();
        }
    }

})


function addMedicineToPrescription(medicineId) {
    $.get('/dashboard/medicine/prescription/add-prescription?medicine_id=' + medicineId + '&count=' + 1).then(res => {
        if(res.status === 'success'){
           $('#order-detail-content').html(res.body);
       }
            let timerInterval;
            Swal.fire({
                icon: res.icon,
                title: "اعلان",
                html: res.html,
                timer: 3000,
                timerProgressBar: true,
                didOpen: () => {
                    Swal.showLoading();
                    const timer = Swal.getPopup().querySelector("b");
                    timerInterval = setInterval(() => {
                        timer.textContent = `${Swal.getTimerLeft()}`;
                    }, 100);
                },
                willClose: () => {
                    clearInterval(timerInterval);
                }
            });

    });
}

function removeOrderDetail(detailId){
    $.get('/dashboard/medicine/prescription/remove-prescription-detail?detail_id=' + detailId).then(res => {
       if(res.status === 'success'){
           $('#order-detail-content').html(res.body);
       }
    });
}

function changePrescriptionDetailCount(detailId, state){
    $.get('/dashboard/medicine/prescription/change-prescription-detail-count?detail_id=' + detailId + '&state=' + state).then(res => {
       if(res.status === 'success'){
           $('#order-detail-content').html(res.body);
       }
    });
}