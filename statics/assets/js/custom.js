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
        getData(url = "/api/patients/?") {
            var self = this;
            if(!url.includes("http")){
            url = "http://" + window.location.host + url
            }
            let myurl = new URL(url);
            if (self.search) {
                myurl.searchParams.set("search", self.search)
                url = myurl.href
            }
            $.get(url)
                .done(function (response) {
                    self.random_lists = response.results;
                    self.next = response.next;
                    self.previous = response.previous;



                    self.current_page = myurl.searchParams.get('page') ? parseInt(myurl.searchParams.get('page')) : 1;

                    self.total_pages = Math.ceil(response.count / 10);
                    self.page_numbers = Array.from({length: self.total_pages}, (_, i) => i + 1);
                })
                .fail(function (error) {
                    console.error("خطا در دریافت داده", error)
                });
        },
        goToPage(page) {
            let url = `/api/patients/?page=${page}`;

            if (this.search) {
                url += `&`;
            }
            this.getData(url);
        },
        nextPage(page) {
            if (this.next) {
                let url = `/api/medicines/?page=${page+1}`;
                this.getData(url);
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
        getData(url = "/api/medicines/?") {
            var self = this;
            if(!url.includes("http")){
            url = "http://" + window.location.host + url
            }
            let myurl = new URL(url);
            if (self.search) {
                myurl.searchParams.set("search", self.search)
                url = myurl.href
            }
            $.get(url)
                .done(function (response) {
                    self.random_lists = response.results;
                    self.next = response.next;
                    self.previous = response.previous;


                    self.current_page = myurl.searchParams.get('page') ? parseInt(myurl.searchParams.get('page')) : 1;

                    self.total_pages = Math.ceil(response.count / 10);
                    self.page_numbers = Array.from({length: self.total_pages}, (_, i) => i + 1);
                })
                .fail(function (error) {
                    console.error("خطا در دریافت داده", error)
                });
        },
        goToPage(page) {
            let url = `/api/medicines/?page=${page}`;

            if (this.search) {
                url += `&`;
            }
            this.getData(url);
        },
        nextPage(page) {
            if (this.next) {
                let url = `/api/medicines/?page=${page+1}`;
                this.getData(url);
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
    el: "#app3",
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
        getData(url = "/api/prescription/") {
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
            let url = `/api/prescription/?page=${page}`;

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
    el: "#app5",
    data: {
        search: "", // مقدار ورودی جستجو
        patients: [], // لیست بیماران
        loading: false, // وضعیت در حال بارگذاری
    },
    methods: {
        getData() {
            const url = "api/patient-search/";

            // ارسال درخواست به API
            this.loading = true; // فعال کردن وضعیت بارگذاری
            $.get(`${url}?q=${this.search}`)
                .done((response) => {
                    if (response.status === "success") {
                        this.patients = response.data;
                    } else if (response.status === "not_found") {
                        console.log(response.message); // پیام "هیچ بیماری یافت نشد"
                        this.patients = [];
                    }
                })
                .always(() => {
                    this.loading = false; // غیرفعال کردن وضعیت بارگذاری
                });
        },
        selectPatient(patient) {
            // وقتی کاربر یک بیمار را انتخاب می‌کند
            if (patient && patient.code && patient.first_name && patient.last_name) {
                let timerInterval;
                Swal.fire({
                    icon: 'success',
                    title: "اعلان",
                    html: `بیمار ${patient.code}-${patient.first_name + ' ' + patient.last_name} با موفقیت انتخاب شد`,
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
                this.search = `${patient.code}`; // نمایش بیمار انتخاب‌شده در input
            }
            this.patients = []; // پاک کردن لیست نتایج
        },
    },
});


function addMedicineToPrescription(medicineId) {
    $.get('/dashboard/medicine/prescription/add-prescription?medicine_id=' + medicineId + '&count=' + 1).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
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
        }


    });
}

function removeOrderDetail(detailId) {
    $.get('/dashboard/medicine/prescription/remove-prescription-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

function changePrescriptionDetailCount(detailId, state) {
    $.get('/dashboard/medicine/prescription/change-prescription-detail-count?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
            // $('#patient').val(medicineId)
            console.log('ali')
        }
    });
}

function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue;
}

$(document).ready(function () {
    $('#check-patient-form').on('submit', function (e) {
        e.preventDefault(); // جلوگیری از ارسال پیش‌فرض فرم

        const patientCode = $('#patient').val(); // دریافت کد ملی از input
        console.log(patientCode)
        const csrfToken = getCSRFToken(); // دریافت توکن CSRF

        $.ajax({
            url: 'submit-prescription/',
            type: 'POST',
            data: {
                patient: patientCode,
            },
            headers: {
                'X-CSRFToken': csrfToken // اضافه کردن توکن CSRF به هدر درخواست
            },
            success: function (res) {
                if (res.status === 'success') {
                    $('#order-detail-content').html(res.body);
                    let timerInterval;
                    Swal.fire({
                        title: "اعلان",
                        icon: res.icon,
                        text: res.message,
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
                }
                else {
                    let timerInterval;
                    Swal.fire({
                        title: "اعلان",
                        icon: res.icon,
                        text: res.message,
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
                }
                if(!patientCode){
                    let timerInterval;
                    Swal.fire({
                        title: "اعلان",
                        icon: 'warning',
                        text: 'لطفا کد ملی را وارد نمایید',
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
                }
            },
            error: function () {
                let timerInterval;
                Swal.fire({
                    title: "اعلان",
                    icon: "خطا در ارتباط",
                    text: "مشکلی در ارسال اطلاعات رخ داده است.",
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
            }
        });
    });
});

