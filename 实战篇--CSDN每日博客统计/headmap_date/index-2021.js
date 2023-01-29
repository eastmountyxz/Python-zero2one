import Chart from "./chart-headmap.js";

d3.json('./data/data-2021.json').then(function(data){

    /* ----------------------------配置参数------------------------  */
    const chart = new Chart();
    const config = {
        margins: {top: 80, left: 50, bottom: 50, right: 50},
        textColor: 'black',
        title: '2021年博客创作热力图（106篇）',
        hoverColor: 'red',
        startTime: '2021-01-01',
        endTime: '2021-12-31',
        cellWidth: 20,
        cellHeight: 20,
        cellPadding: 1,
        cellColor1: '#F5F5F5',
        cellColor2: 'green',
        lineColor: 'yellow',
        lineWidth: 2
    }

    chart.margins(config.margins);

    /* ----------------------------初始化常量------------------------  */
    const startTime = new Date(config.startTime);
    const endTime = new Date(config.endTime);
    const widthOffset = config.cellWidth + config.cellPadding;
    const heightOffset = config.cellHeight + config.cellPadding;

    /* ----------------------------颜色转换------------------------  */
    chart.scaleColor = d3.scaleLinear()
                            .domain([0, d3.max(Object.values(data))])
                            .range([config.cellColor1, config.cellColor2]);

    /* ----------------------------渲染矩形------------------------  */
    chart.renderRect = function(){
        let currentYear, currentMonth;
        let yearGroup, monthGroup;
        const initDay = startTime.getDay();
        let currentDay = initDay;
        const totalDays = getTotalDays(startTime, endTime) + initDay;	
	console.info(totalDays);

        const mainBody = chart.body()
                                .append('g')
                                .attr('class', 'date')
                                .attr('transform', 'translate(' + 35 + ',' + 50 + ')')

        while(currentDay <= totalDays){
            let currentDate = getDate(startTime, currentDay).split('-');

            if(!currentYear || currentDate[0] !== currentYear){
                currentYear = currentDate[0];

                yearGroup = mainBody
                                .append('g')
                                .attr('class', 'year ' + currentYear);
            }

            if (!currentMonth || currentDate[1] !== currentMonth){
                currentMonth = currentDate[1];

                monthGroup = yearGroup.append('g').attr('class', 'month ' + currentMonth);
            }

            monthGroup
                 .append('g')
                 .attr('class', 'g ' + currentDate.join('-'))
                 .datum(currentDate.join('-'))
                 .append('rect')
                 .attr('width', config.cellWidth)
                 .attr('height', config.cellHeight)
                 .attr('x', Math.floor(currentDay / 7) * widthOffset)
                 .attr('y', currentDay % 7 * heightOffset);

            currentDay++;
        }

        d3.selectAll('.g')
            .each(function(d){
                d3.select(this)
                    .attr('fill', chart.scaleColor(data[d] || 0))
                    .datum({time: d, value: data[d] || 0});
            });

        function getTotalDays(startTime, endTime){
            return Math.floor((endTime.getTime() - startTime.getTime()) / 86400000);
        }

        function getDate(startTime, day){
            const date =  new Date(startTime.getTime() + 86400000 * (day - initDay));
            return d3.timeFormat("%Y-%m-%d")(date);
        }
    }

    /* ----------------------------渲染分隔线------------------------  */
    chart.renderLine = function(){
        const initDay = startTime.getDay();
        const days = [initDay-1];
        const linePaths = getLinePath();

        d3.select('.date')
                .append('g')
                .attr('class', 'lines')
                .selectAll('path')
                .data(linePaths)
                .enter()
                .append('path')
                .attr('stroke', config.lineColor)
                .attr('stroke-width', config.lineWidth)
                .attr('fill', 'none')
                .attr('d', (d) => d);

        function getLinePath(){
            const paths = [];

            d3.selectAll('.month')
                .each(function(d,i){
                    days[i+1] = days[i] + this.childNodes.length;
                });

            days.forEach((day,i) => {
                let path = 'M';
                let weekDay = day < 0 ? 6 : day % 7;

                if (weekDay !== 6) {
                    path += Math.floor(day / 7) * widthOffset + ' ' + 7 * heightOffset;
                    path +=  ' l' + '0' + ' ' + (weekDay - 6) * heightOffset;
                    path += ' l' + widthOffset + ' ' + '0';
                    path += ' l' + '0' + ' ' + (-weekDay - 1) * heightOffset;
                } else {
                    path += (Math.floor(day / 7) + 1) * widthOffset + ' ' + 7 * heightOffset;
                    path +=  ' l' + '0' + ' ' + (-7) * heightOffset;
                }

                paths.push(path);
            });

            return paths;
        }

    }

    /* ----------------------------渲染文本标签------------------------ */
    chart.renderText = function(){
        let week = ['Sun', 'Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat'];

        d3.select('.year')
            .append('g')
            .attr('class', 'week')
            .selectAll('.label')
            .data(week)
            .enter()
            .append('text')
            .attr('class', 'label')
            .attr('x', -40)
            .attr('y', heightOffset/2)
            .attr('dy', (d,i) => i * heightOffset + 4)
            .text((d)=>d);

        let months = d3.timeMonth.range(new Date(startTime.getFullYear(), startTime.getMonth(), startTime.getDate()), new Date(endTime.getFullYear(), endTime.getMonth(), endTime.getDate()));

        months = months.map((d) => d3.timeFormat("%b")(d));

        d3.select('.year')
            .append('g')
            .attr('class', 'month-label')
            .selectAll('text')
            .data(months)
            .enter()
            .append('text')
            .attr('x', (d,i) => i*widthOffset*4.25 + widthOffset*2)
            .attr('y', -10)
            .text((d) => d)

    }

    /* ----------------------------渲染图标题------------------------  */
    chart.renderTitle = function(){

        chart.svg().append('text')
                .classed('title', true)
                .attr('x', chart.width()/2)
                .attr('y', 0)
                .attr('dy', '2em')
                .text(config.title)
                .attr('fill', config.textColor)
                .attr('text-anchor', 'middle')
                .attr('stroke', config.textColor);

    }

    /* ----------------------------绑定鼠标交互事件------------------------  */
    chart.addMouseOn = function(){
        //防抖函数
        function debounce(fn, time){
            let timeId = null;
            return function(){
                const context = this;
                const event = d3.event;
                timeId && clearTimeout(timeId)
                timeId = setTimeout(function(){
                    d3.event = event;
                    fn.apply(context, arguments);
                }, time);
            }
        }

        d3.selectAll('.g')
            .on('mouseenter', function(d){
                const e = d3.event;
                const position = d3.mouse(chart.svg().node());

                d3.select(e.target)
                    .attr('fill', config.hoverColor);

                chart.svg()
                    .append('text')
                    .classed('tip', true)
                    .attr('x', position[0]+5)
                    .attr('y', position[1])
                    .attr('fill', config.textColor)
                    .text(d.time);
            })
            .on('mouseleave', function(d){
                const e = d3.event;

                d3.select(e.target)
                    .attr('fill', chart.scaleColor(d.value));

                d3.select('.tip').remove();
            })
            .on('mousemove', debounce(function(){
                    const position = d3.mouse(chart.svg().node());
                    d3.select('.tip')
                    .attr('x', position[0]+5)
                    .attr('y', position[1]-5);
                }, 6)
            );
    }

    chart.render = function(){

        chart.renderTitle();

        chart.renderRect();

        chart.renderLine();

        chart.renderText();

        chart.addMouseOn();

    }

    chart.renderChart();


});














