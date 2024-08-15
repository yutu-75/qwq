"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[95843],{95843:(e,t,a)=>{a.r(t),a.d(t,{default:()=>ee});var i=a(667294),s=a(943323),o=a(751995),n=a(45697),r=a.n(n),l=a(823493),c=a.n(l),h=a(121804),m=a.n(h),d=a(615078),u=a.n(d),p=a(730381),y=a.n(p),x=a(728041),g=a.n(x),b=a(328062),f=a(767190),k=a(455867),w=a(281928),v=a(645636),A=a(751115),L=a(740962),M=a(237731),C=a(760524),D=(a(569175),a(195963)),T=a(383937),$=a(880221);const S=r().oneOfType([r().number,r().oneOf(["auto"])]),F=r().oneOfType([r().string,r().shape({label:r().string})]),_=r().shape({r:r().number.isRequired,g:r().number.isRequired,b:r().number.isRequired}),N=r().shape({x:r().number,y:r().number}),O=r().shape({x:r().string,y:r().number}),E=r().shape({outliers:r().arrayOf(r().number),Q1:r().number,Q2:r().number,Q3:r().number,whisker_high:r().number,whisker_low:r().number}),B=r().shape({markerLabels:r().arrayOf(r().string),markerLineLabels:r().arrayOf(r().string),markerLines:r().arrayOf(r().number),markers:r().arrayOf(r().number),measures:r().arrayOf(r().number),rangeLabels:r().arrayOf(r().string),ranges:r().arrayOf(r().number)}),Z=r().shape({annotationType:r().oneOf(Object.keys(D.DT)),color:r().string,hideLine:r().bool,name:r().string,opacity:r().string,show:r().bool,showMarkers:r().bool,sourceType:r().string,style:r().string,value:r().oneOfType([r().number,r().string]),width:r().number}),z=[{text:"No data",dy:"-.75em",class:"header"},{text:"Adjust filters or check the Datasource.",dy:".75em",class:"body"}];g().utils.noData=function(e,t){const a=e.options().margin(),i=g().utils.availableHeight(null,t,a),s=g().utils.availableWidth(null,t,a),o=a.left+s/2,n=a.top+i/2;t.selectAll("g").remove();const r=t.selectAll(".nv-noData").data(z);r.enter().append("text").attr("class",(e=>`nvd3 nv-noData ${e.class}`)).attr("dy",(e=>e.dy)).style("text-anchor","middle"),r.attr("x",o).attr("y",n).text((e=>e.text))};const{getColor:I,getScale:R}=b,G=340,P=["line","dual_line","line_multi","area","compare","bar","time_pivot"],U={data:r().oneOfType([r().arrayOf(r().oneOfType([O,r().shape({key:r().string,values:r().arrayOf(O)}),r().shape({key:r().arrayOf(r().string),values:r().arrayOf(N)}),r().shape({classed:r().string,key:r().string,type:r().string,values:r().arrayOf(N),yAxis:r().number}),r().shape({label:r().string,values:r().arrayOf(E)}),r().shape({key:r().string,values:r().arrayOf(r().object)})])),B]),width:r().number,height:r().number,annotationData:r().object,annotationLayers:r().arrayOf(Z),bottomMargin:S,colorScheme:r().string,comparisonType:r().string,contribution:r().bool,leftMargin:S,onError:r().func,showLegend:r().bool,showMarkers:r().bool,useRichTooltip:r().bool,vizType:r().oneOf(["area","bar","box_plot","bubble","bullet","compare","column","dist_bar","line","line_multi","time_pivot","pie","dual_line"]),xAxisFormat:r().string,numberFormat:r().string,xAxisLabel:r().string,xAxisShowMinMax:r().bool,xIsLogScale:r().bool,xTicksLayout:r().oneOf(["auto","staggered","45\xb0"]),yAxisFormat:r().string,yAxisBounds:r().arrayOf(r().number),yAxisLabel:r().string,yAxisShowMinMax:r().bool,yIsLogScale:r().bool,orderBars:r().bool,isBarStacked:r().bool,showBarValue:r().bool,reduceXTicks:r().bool,showControls:r().bool,showBrush:r().oneOf([!0,"yes",!1,"no","auto"]),onBrushEnd:r().func,yAxis2Format:r().string,lineInterpolation:r().string,isDonut:r().bool,isPieLabelOutside:r().bool,pieLabelType:r().oneOf(["key","value","percent","key_value","key_percent","key_value_percent"]),showLabels:r().bool,areaStackedStyle:r().string,entity:r().string,maxBubbleSize:r().number,xField:F,yField:F,sizeField:F,baseColor:_},V=()=>{},W=(0,f.JB)();function H(e,t){const{queriesData:a,groupby:i,data:s,width:o,height:n,annotationData:r,annotationLayers:l=[],areaStackedStyle:h,baseColor:d,bottomMargin:p,colorScheme:x,comparisonType:b,contribution:S,drillDown:F,enableDrilldown:_,drilldownColumns:N,entity:O,isBarStacked:E,isDonut:B,isPieLabelOutside:Z,leftMargin:z,lineInterpolation:U="linear",markerLabels:H,markerLines:J,markerLineLabels:q,markers:j,maxBubbleSize:X,onBrushEnd:Q=V,onError:Y=V,orderBars:K,ownState:ee,pieLabelType:te,rangeLabels:ae,ranges:ie,reduceXTicks:se=!1,setDataMask:oe,showBarValue:ne,showBrush:re,showControls:le,showLabels:ce,showLegend:he,showMarkers:me,sizeField:de,useRichTooltip:ue,vizType:pe,xAxisFormat:ye,numberFormat:xe,xAxisLabel:ge,xAxisShowMinMax:be=!1,xField:fe,xIsLogScale:ke,xTicksLayout:we,yAxisFormat:ve,yAxis2Format:Ae,yAxisBounds:Le,yAxis2Bounds:Me,yAxisLabel:Ce,yAxisShowMinMax:De=!1,yAxis2ShowMinMax:Te=!1,yField:$e,yIsLogScale:Se,sliceId:Fe}=t,_e=null!==document.querySelector("#explorer-container"),Ne=e;Ne.innerHTML="";const Oe=l.filter((e=>e.show));let Ee,Be=Ne,Ze=null;for(;Be.parentElement;){if(Be.parentElement.id.startsWith("chart-id-")){Ze=Be.parentElement.id;break}Be=Be.parentElement}let ze=o,Ie="key";function Re(e){return e.includes(pe)}Ne.style.width=`${o}px`,Ne.style.height=`${n}px`;Ze?(0,$.o2)(Ze):(0,$.Vl)(!0),g().addGraph((function(){const t=u().select(e);t.classed("superset-legacy-chart-nvd3",!0),t.classed(`superset-legacy-chart-nvd3-${m()(pe)}`,!0);let a=t.select("svg");a.empty()&&(a=t.append("svg"));const i="bullet"===pe?Math.min(n,50):n,l=Re(P),_="staggered"===we,N="auto"===we&&Re(["column","dist_bar"])||"45\xb0"===we?45:0;if(45===N&&(0,T.Z)(re))return Y((0,k.t)("You cannot use 45\xb0 tick layout along with the time range filter")),null;const Ne=(0,T.Z)(re)||"auto"===re&&n>=480&&"45\xb0"!==we,Be=(0,f.JB)(xe);switch(pe){case"line":Ne?(Ee=g().models.lineWithFocusChart(),_&&(Ee.focus.margin({bottom:40}),Ee.focusHeight(80)),Ee.focus.xScale(u().time.scale.utc())):Ee=g().models.lineChart(),Ee.xScale(u().time.scale.utc()),Ee.interpolate(U),Ee.clipEdge(!1);break;case"time_pivot":Ee=g().models.lineChart(),Ee.xScale(u().time.scale.utc()),Ee.interpolate(U);break;case"dual_line":case"line_multi":Ee=g().models.multiChart(),Ee.interpolate(U),Ee.xScale(u().time.scale.utc());break;case"bar":Ee=g().models.multiBarChart().showControls(le).groupSpacing(.1),se||(ze=(0,$.UG)(s,E,o)),Ee.width(ze),Ee.xAxis.showMaxMin(!1),Ee.stacked(E);break;case"dist_bar":Ee=g().models.multiBarChart().showControls(le).reduceXTicks(se).groupSpacing(.1),Ee.xAxis.showMaxMin(!1),Ee.stacked(E),K&&s.forEach((e=>{const t=[...e.values];e.values=t.sort(((e,t)=>(0,$.Hy)(e.x)<(0,$.Hy)(t.x)?-1:1))})),se||(ze=(0,$.UG)(s,E,o)),Ee.width(ze),Ee.multibar.dispatch.on("elementClick",(e=>{if(F&&null!=ee&&ee.drilldown){const t=e.data.x,a=w.Z.drillDown(null==ee?void 0:ee.drilldown,t);oe({extraFormData:{filters:a.filters},filterState:{value:t&&a.filters.length>0?[t]:null},ownState:{drilldown:a}})}}));break;case"pie":if(Ee=g().models.pieChart(),Ie="x",Ee.valueFormat(Be),B&&Ee.donut(!0),Ee.showLabels(ce),Ee.labelsOutside(Z),Ee.labelThreshold(.05),Ee.cornerRadius(!0),["key","value","percent"].includes(te))Ee.labelType(te);else if("key_value"===te)Ee.labelType((e=>`${e.data.x}: ${Be(e.data.y)}`));else{const e=u().sum(s,(e=>e.y)),t=(0,f.JB)(v.Z.PERCENT_2_POINT);"key_percent"===te?(Ee.tooltip.valueFormatter((e=>t(e))),Ee.labelType((a=>`${a.data.x}: ${t(a.data.y/e)}`))):(Ee.tooltip.valueFormatter((a=>`${Be(a)} (${t(a/e)})`)),Ee.labelType((a=>`${a.data.x}: ${Be(a.data.y)} (${t(a.data.y/e)})`)))}Ee.margin({top:0});break;case"column":Ee=g().models.multiBarChart().reduceXTicks(!1);break;case"compare":Ee=g().models.cumulativeLineChart(),Ee.xScale(u().time.scale.utc()),Ee.useInteractiveGuideline(!0),Ee.xAxis.showMaxMin(!1);break;case"bubble":Ee=g().models.scatterChart(),Ee.showDistX(!1),Ee.showDistY(!1),Ee.tooltip.contentGenerator((e=>(0,$.zK)({point:e.point,entity:O,xField:fe,yField:$e,sizeField:de,xFormatter:(0,$.fF)(ye),yFormatter:(0,$.fF)(ve),sizeFormatter:W}))),Ee.pointRange([5,X**2]),Ee.pointDomain([0,u().max(s,(e=>u().max(e.values,(e=>e.size))))]);break;case"area":Ee=g().models.stackedAreaChart(),Ee.showControls(le),Ee.style(h),Ee.xScale(u().time.scale.utc());break;case"box_plot":Ie="label",Ee=g().models.boxPlotChart(),Ee.x((e=>e.label)),Ee.maxBoxWidth(75);break;case"bullet":Ee=g().models.bulletChart(),s.rangeLabels=ae,s.ranges=ie,s.markerLabels=H,s.markerLines=J,s.markerLineLabels=q,s.markers=j;break;default:throw new Error(`Unrecognized visualization for nvd3${pe}`)}let Ge;if(Ee.margin({left:0,bottom:0}),ne&&((0,$.Ad)(a,s,E,ve),Ee.dispatch.on("stateChange.drawBarValues",(()=>{(0,$.Ad)(a,s,E,ve)}))),Ne&&Q!==V&&Ee.focus&&Ee.focus.dispatch.on("brush",(e=>{const t=(0,$.z_)(e.extent);t&&e.brush.on("brushend",(()=>{Q(t)}))})),Ee.xAxis&&Ee.xAxis.staggerLabels&&Ee.xAxis.staggerLabels(_),Ee.xAxis&&Ee.xAxis.rotateLabels&&Ee.xAxis.rotateLabels(N),Ee.x2Axis&&Ee.x2Axis.staggerLabels&&Ee.x2Axis.staggerLabels(_),Ee.x2Axis&&Ee.x2Axis.rotateLabels&&Ee.x2Axis.rotateLabels(N),"showLegend"in Ee&&"undefined"!==typeof he&&(ze<G&&"pie"!==pe?Ee.showLegend(!1):Ee.showLegend(he)),Se&&Ee.yScale(u().scale.log()),ke&&Ee.xScale(u().scale.log()),l?(Ge=(0,A.bt)(ye),Ee.interactiveLayer.tooltip.headerFormatter(L.Z)):Ge=(0,$.fF)(ye),Ee.x2Axis&&Ee.x2Axis.tickFormat&&Ee.x2Axis.tickFormat(Ge),Ee.xAxis&&Ee.xAxis.tickFormat){Re(["dist_bar","box_plot"])?Ee.xAxis.tickFormat((e=>e.length>40?`${e.slice(0,Math.max(0,40))}\u2026`:e)):Ee.xAxis.tickFormat(Ge)}let Pe=(0,$.fF)(ve);if(Ee.yAxis&&Ee.yAxis.tickFormat&&(!S&&"percentage"!==b||ve&&ve!==v.Z.SMART_NUMBER&&ve!==v.Z.SMART_NUMBER_SIGNED||(Pe=(0,f.JB)(v.Z.PERCENT_1_POINT)),Ee.yAxis.tickFormat(Pe)),Ee.y2Axis&&Ee.y2Axis.tickFormat&&Ee.y2Axis.tickFormat(Pe),Ee.yAxis&&Ee.yAxis.ticks(5),Ee.y2Axis&&Ee.y2Axis.ticks(5),(0,$.Ml)(Ee.xAxis,be),(0,$.Ml)(Ee.x2Axis,be),(0,$.Ml)(Ee.yAxis,De),(0,$.Ml)(Ee.y2Axis,Te||De),"time_pivot"===pe){if(d){const{r:e,g:t,b:a}=d;Ee.color((i=>{const s=i.rank>0?.5*i.perc:1;return`rgba(${e}, ${t}, ${a}, ${s})`}))}Ee.useInteractiveGuideline(!0),Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.RO)(e,Ge,Pe)))}else if("bullet"!==pe){const e=R(x);Ee.color((t=>t.color||e((0,$.gO)(t[Ie]),Fe)))}if(Re(["line","area","bar","dist_bar"])&&ue&&(Ee.useInteractiveGuideline(!0),"line"===pe||"bar"===pe?Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.Gx)(e,L.Z,Pe))):"dist_bar"===pe?Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.yy)(e,Pe))):Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.n4)(e,L.Z,Pe,Ee)))),Re(["compare"])&&Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.yy)(e,Pe))),Re(["dual_line","line_multi"])){const e=(0,f.JB)(ve),t=(0,f.JB)(Ae);Ee.yAxis1.tickFormat(e),Ee.yAxis2.tickFormat(t);const a=s.map((a=>1===a.yAxis?e:t));Ee.useInteractiveGuideline(!0),Ee.interactiveLayer.tooltip.contentGenerator((e=>(0,$.HO)(e,Ge,a)))}if(Ee.width(ze),Ee.height(i),a.datum(s).transition().duration(500).attr("height",i).attr("width",ze).call(Ee),Se&&Ee.yAxis.tickFormat((e=>0!==e&&Math.log10(e)%1===0?Pe(e):"")),N>0){a.select(".nv-x.nv-axis > g").selectAll("g").selectAll("text").attr("dx",-6.5)}const Ue=()=>{if(Ee.yDomain&&Array.isArray(Le)&&2===Le.length){const[e,t]=Le,a=(0,M.Z)(e)&&!Number.isNaN(e),i=(0,M.Z)(t)&&!Number.isNaN(t);if((a||i)&&"area"===pe&&"expand"===Ee.style())Ee.yDomain([0,1]);else if((a||i)&&"area"===pe&&"stream"===Ee.style())Ee.yDomain((0,$.po)(s));else if(a&&i)Ee.yDomain([e,t]),Ee.clipEdge(!0);else if(a||i){let[o,n]=[0,1];"area"===pe||Re(["bar","dist_bar"])&&Ee.stacked()?[o,n]=(0,$.po)(s):[o,n]=(0,$.tH)(s);const r=a?e:o,l=i?t:n;Ee.yDomain([r,l]),Ee.clipEdge(!0)}}};if(Ue(),Ee.dispatch&&Ee.dispatch.stateChange&&Ee.dispatch.on("stateChange.applyYAxisBounds",Ue),Re(["dual_line","line_multi"])){const e=Ee.yAxis1.ticks(),t=Ee.yAxis1.scale().domain(Ee.yAxis1.domain()).nice(e).ticks(e),a=Ee.yAxis2.scale().domain(Ee.yAxis2.domain()).nice(e).ticks(e),i=t.length-a.length;if(t.length>0&&a.length>0&&0!==i){const e=i<0?t:a,s=e[1]-e[0];for(let t=0;t<Math.abs(i);t+=1)t%2===0?e.unshift(e[0]-s):e.push(e[e.length-1]+s);Ee.yDomain1([t[0],t[t.length-1]]),Ee.yDomain2([a[0],a[a.length-1]]),Ee.yAxis1.tickValues(t),Ee.yAxis2.tickValues(a)}Ee.yDomain1([Le[0]||t[0],Le[1]||t[t.length-1]]),Ee.yDomain2([Me[0]||a[0],Me[1]||a[a.length-1]])}if(me&&(a.selectAll(".nv-point").style("stroke-opacity",1).style("fill-opacity",1),Ee.dispatch.on("stateChange.showMarkers",(()=>{setTimeout((()=>{a.selectAll(".nv-point").style("stroke-opacity",1).style("fill-opacity",1)}),10)}))),void 0!==Ee.yAxis||void 0!==Ee.yAxis2){const t=Math.ceil(Math.min(o*(_e?.01:.03),30)),n=Ee.margin();Ee.xAxis&&(n.bottom=28);const h=(0,$.GF)(a,Ee.yAxis2?"nv-y1":"nv-y"),m=(0,$.GF)(a,"nv-x");if(n.left=h+t,Ce&&""!==Ce&&(n.left+=25),ne&&(n.top+=24),be&&(n.right=Math.max(20,m/2)+t),45===N?(n.bottom=m*Math.sin(Math.PI*N/180)+t+30,n.right=m*Math.cos(Math.PI*N/180)+t):_&&(n.bottom=40),Re(["dual_line","line_multi"])){const e=(0,$.GF)(a,"nv-y2");n.right=e+t}if(p&&"auto"!==p&&(n.bottom=parseInt(p,10)),z&&"auto"!==z&&(n.left=z),ge&&""!==ge&&Ee.xAxis){n.bottom+=25;let e=0;n.bottom&&!Number.isNaN(n.bottom)&&(e=n.bottom-45),Ee.xAxis.axisLabel(ge).axisLabelDistance(e)}if(Ce&&""!==Ce&&Ee.yAxis){let e=0;n.left&&!Number.isNaN(n.left)&&(e=n.left-70),Ee.yAxis.axisLabel(Ce).axisLabelDistance(e)}if(l&&r&&Oe.length>0){const e=Oe.filter((e=>e.annotationType===D.ZP.TIME_SERIES)).reduce(((e,t)=>e.concat((r[t.name]||[]).map((e=>{if(!e)return{};const a=Array.isArray(e.key)?`${t.name}, ${e.key.join(", ")}`:`${t.name}, ${e.key}`;return{...e,key:a,color:t.color,strokeWidth:t.width,classed:`${t.opacity} ${t.style} nv-timeseries-annotation-layer showMarkers${t.showMarkers} hideLine${t.hideLine}`}})))),[]);s.push(...e)}if(Ze&&(Ee&&Ee.interactiveLayer&&Ee.interactiveLayer.tooltip&&Ee.interactiveLayer.tooltip.classes([(0,$.T7)(Ze)]),Ee&&Ee.tooltip&&Ee.tooltip.classes([(0,$.T7)(Ze)])),Ee.margin(n),a.datum(s).transition().duration(500).attr("width",ze).attr("height",i).call(Ee),window.addEventListener("scroll",c()((()=>(0,$.Vl)(!1)),250)),l&&Oe.length>0){const t=Oe.filter((e=>e.annotationType===D.ZP.FORMULA));let o,n,l;if("bar"===pe?(n=u().min(s[0].values,(e=>e.x)),o=u().max(s[0].values,(e=>e.x)),l=u().scale.quantile().domain([n,o]).range(Ee.xAxis.range())):(n=Ee.xAxis.scale().domain()[0].valueOf(),o=Ee.xAxis.scale().domain()[1].valueOf(),l=Ee.xScale?Ee.xScale():Ee.xAxis.scale?Ee.xAxis.scale():u().scale.linear()),l&&l.clamp&&l.clamp(!0),t.length>0){const e=[];if("bar"===pe){const t=s.reduce(((e,t)=>(t.values.forEach((t=>e.add(t.x))),e)),new Set);e.push(...t.values()),e.sort()}else{let t=Math.min(...s.map((e=>Math.min(...e.values.slice(1).map(((t,a)=>t.x-e.values[a].x))))));const a=(o-n)/(t||1);t=a<100?(o-n)/100:t,t=a>500?(o-n)/500:t,e.push(n);for(let a=n;a<o;a+=t)e.push(a);e.push(o)}const a=t.map((t=>{const{value:a}=t;return{key:t.name,values:e.map((e=>({x:e,y:(0,C.f)(a,e)}))),color:t.color,strokeWidth:t.width,classed:`${t.opacity} ${t.style}`}}));s.push(...a)}const c=Ee.xAxis1?Ee.xAxis1:Ee.xAxis,h=Ee.yAxis1?Ee.yAxis1:Ee.yAxis,m=c.scale().range()[1],d=h.scale().range()[0];r&&(Oe.filter((e=>e.annotationType===D.ZP.EVENT&&r&&r[e.name])).forEach(((t,a)=>{const i=(0,D.yb)(t),s=u().select(e).select(".nv-wrap").append("g").attr("class",`nv-event-annotation-layer-${a}`),o=i.color||I((0,$.gO)(i.name),x),n=(0,$.Gr)({...i,annotationTipClass:`arrow-down nv-event-annotation-layer-${t.sourceType}`}),c=(r[i.name].records||[]).map((e=>{const t=new Date(y().utc(e[i.timeColumn]));return{...e,[i.timeColumn]:t}})).filter((e=>!Number.isNaN(e[i.timeColumn].getMilliseconds())));c.length>0&&s.selectAll("line").data(c).enter().append("line").attr({x1:e=>l(new Date(e[i.timeColumn])),y1:0,x2:e=>l(new Date(e[i.timeColumn])),y2:d}).attr("class",`${i.opacity} ${i.style}`).style("stroke",o).style("stroke-width",i.width).on("mouseover",n.show).on("mouseout",n.hide).call(n),Ee.focus&&Ee.focus.dispatch.on("onBrush.event-annotation",(()=>{s.selectAll("line").data(c).attr({x1:e=>l(new Date(e[i.timeColumn])),y1:0,x2:e=>l(new Date(e[i.timeColumn])),y2:d,opacity:e=>{const t=l(new Date(e[i.timeColumn]));return t>0&&t<m?1:0}})}))})),Oe.filter((e=>e.annotationType===D.ZP.INTERVAL&&r&&r[e.name])).forEach(((t,a)=>{const i=(0,D.yb)(t),s=u().select(e).select(".nv-wrap").append("g").attr("class",`nv-interval-annotation-layer-${a}`),o=i.color||I((0,$.gO)(i.name),x),n=(0,$.Gr)(i),c=(r[i.name].records||[]).map((e=>{const t=new Date(y().utc(e[i.timeColumn])),a=new Date(y().utc(e[i.intervalEndColumn]));return{...e,[i.timeColumn]:t,[i.intervalEndColumn]:a}})).filter((e=>!Number.isNaN(e[i.timeColumn].getMilliseconds())&&!Number.isNaN(e[i.intervalEndColumn].getMilliseconds())));c.length>0&&s.selectAll("rect").data(c).enter().append("rect").attr({x:e=>Math.min(l(new Date(e[i.timeColumn])),l(new Date(e[i.intervalEndColumn]))),y:0,width:e=>Math.max(Math.abs(l(new Date(e[i.intervalEndColumn]))-l(new Date(e[i.timeColumn]))),1),height:d}).attr("class",`${i.opacity} ${i.style}`).style("stroke-width",i.width).style("stroke",o).style("fill",o).style("fill-opacity",.2).on("mouseover",n.show).on("mouseout",n.hide).call(n),Ee.focus&&Ee.focus.dispatch.on("onBrush.interval-annotation",(()=>{s.selectAll("rect").data(c).attr({x:e=>l(new Date(e[i.timeColumn])),width:e=>{const t=l(new Date(e[i.timeColumn]));return l(new Date(e[i.intervalEndColumn]))-t}})}))}))),a.datum(s).attr("height",i).attr("width",ze).call(Ee),Ee.dispatch.on("renderEnd.timeseries-annotation",(()=>{u().selectAll(".slice_container .nv-timeseries-annotation-layer.showMarkerstrue .nv-point").style("stroke-opacity",1).style("fill-opacity",1),u().selectAll(".slice_container .nv-timeseries-annotation-layer.hideLinetrue").style("stroke-width",0)}))}}return(0,$.Aw)(Ee),Ee}))}H.displayName="NVD3",H.propTypes=U;const J=H;var q=a(435247);const j="cglaEQm3J3TF07nAh29A";var X=a(211965);const Q=e=>{const{ownState:t,drilldownColumns:a,enableDrilldown:s,setDataMask:o}=e,n=a?a.length:0,[r,l]=(0,i.useState)(a||[]);(0,i.useEffect)((()=>{Object.keys(t||{}).length>0&&l(t.groupBy)}),[JSON.stringify(t)]);return s&&null!=r&&r.length?(0,X.tZ)(q.Z,{className:j},r.map(((e,a)=>(0,X.tZ)(q.Z.Item,{onClick:()=>((e,a)=>{if(a!==n-1&&n>1){const i=((null==t?void 0:t.filters)||[]).slice(0,a),s=((null==t?void 0:t.groupBy)||[]).slice(0,a+1);o({extraFormData:{filters:i},filterState:{value:e&&i.length>0?[e]:null},ownState:{index:a+1,filters:i,groupBy:s}})}})(e,a),key:`${e}`},e)))):null};const Y=(0,s.Z)(J,{componentWillUnmount:function(){const{id:e}=this.props;null!==e&&void 0!==e?(0,$.o2)(e):(0,$.Vl)(!0)}}),K=({className:e,...t})=>(0,X.tZ)("div",{className:e},(0,X.tZ)(Q,{ownState:t.ownState,setDataMask:t.setDataMask,drilldownColumns:t.drilldownColumns,enableDrilldown:t.enableDrilldown}),(0,X.tZ)(Y,t));K.propTypes={className:r().string.isRequired};const ee=(0,o.iK)(K)`
  .superset-legacy-chart-nvd3-dist-bar,
  .superset-legacy-chart-nvd3-bar {
    overflow-x: auto !important;
    svg {
      &.nvd3-svg {
        width: auto;
        font-size: ${({theme:e})=>e.typography.sizes.m};
      }
    }
  }
  .superset-legacy-chart-nvd3 {
    nv-x text {
      font-size: ${({theme:e})=>e.typography.sizes.m};
    }
    g.superset path {
      stroke-dasharray: 5, 5;
    }
    .nvtooltip tr.highlight td {
      font-weight: ${({theme:e})=>e.typography.weights.bold};
      font-size: ${({theme:e})=>e.typography.sizes.m}px !important;
    }
    text.nv-axislabel {
      font-size: ${({theme:e})=>e.typography.sizes.m} !important;
    }
    g.solid path,
    line.solid {
      stroke-dasharray: unset;
    }
    g.dashed path,
    line.dashed {
      stroke-dasharray: 5, 5;
    }
    g.longDashed path,
    line.dotted {
      stroke-dasharray: 1, 1;
    }

    g.opacityLow path,
    line.opacityLow {
      stroke-opacity: 0.2;
    }

    g.opacityMedium path,
    line.opacityMedium {
      stroke-opacity: 0.5;
    }
    g.opacityHigh path,
    line.opacityHigh {
      stroke-opacity: 0.8;
    }
    g.time-shift-0 path,
    line.time-shift-0 {
      stroke-dasharray: 5, 5;
    }
    g.time-shift-1 path,
    line.time-shift-1 {
      stroke-dasharray: 1, 5;
    }
    g.time-shift-2 path,
    line.time-shift-3 {
      stroke-dasharray: 5, 1;
    }
    g.time-shift-3 path,
    line.time-shift-3 {
      stroke-dasharray: 5, 1;
    }
    g.time-shift-4 path,
    line.time-shift-4 {
      stroke-dasharray: 5, 10;
    }
    g.time-shift-5 path,
    line.time-shift-5 {
      stroke-dasharray: 0.9;
    }
    g.time-shift-6 path,
    line.time-shift-6 {
      stroke-dasharray: 15, 10, 5;
    }
    g.time-shift-7 path,
    line.time-shift-7 {
      stroke-dasharray: 15, 10, 5, 10;
    }
    g.time-shift-8 path,
    line.time-shift-8 {
      stroke-dasharray: 15, 10, 5, 10, 15;
    }
    g.time-shift-9 path,
    line.time-shift-9 {
      stroke-dasharray: 5, 5, 1, 5;
    }
    .nv-noData.body {
      font-size: ${({theme:e})=>e.typography.sizes.m};
      font-weight: ${({theme:e})=>e.typography.weights.normal};
    }
  }
  .superset-legacy-chart-nvd3-tr-highlight {
    border-top: 1px solid;
    border-bottom: 1px solid;
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
  .superset-legacy-chart-nvd3-tr-total {
    font-weight: ${({theme:e})=>e.typography.weights.bold};
  }
  .nvtooltip {
    .tooltip-header {
      white-space: nowrap;
      font-weight: ${({theme:e})=>e.typography.weights.bold};
    }
    tbody tr:not(.tooltip-header) td:nth-child(2) {
      word-break: break-word;
    }
  }
  .d3-tip.nv-event-annotation-layer-table,
  .d3-tip.nv-event-annotation-layer-NATIVE {
    width: 200px;
    border-radius: 2px;
    background-color: ${({theme:e})=>e.colors.grayscale.base};
    fill-opacity: 0.6;
    margin: ${({theme:e})=>2*e.gridUnit}px;
    padding: ${({theme:e})=>2*e.gridUnit}px;
    color: ${({theme:e})=>e.colors.grayscale.light5};
    &:after {
      content: '\\25BC';
      font-size: ${({theme:e})=>e.typography.sizes.m};
      color: ${({theme:e})=>e.colors.grayscale.base};
      position: absolute;
      bottom: -14px;
      left: 94px;
    }
  }
`},943323:(e,t,a)=>{a.d(t,{Z:()=>o});var i=a(667294),s=a(211965);function o(e,t){class a extends i.Component{constructor(e){super(e),this.container=void 0,this.setContainerRef=this.setContainerRef.bind(this)}componentDidMount(){this.execute()}componentDidUpdate(){this.execute()}componentWillUnmount(){this.container=void 0,null!=t&&t.componentWillUnmount&&t.componentWillUnmount.bind(this)()}setContainerRef(e){this.container=e}execute(){this.container&&e(this.container,this.props)}render(){const{id:e,className:t}=this.props;return(0,s.tZ)("div",{ref:this.setContainerRef,id:e,className:t})}}const o=a;return e.displayName&&(o.displayName=e.displayName),e.propTypes&&(o.propTypes={...o.propTypes,...e.propTypes}),e.defaultProps&&(o.defaultProps=e.defaultProps),a}}}]);