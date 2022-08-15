import pygame
import random
import time
pygame.font.init()
pygame.init()
W=980
H=750
sortpoint=0
sort='merge'
surf=pygame.display.set_mode((W,H))
run=True
pic=pygame.image.load("thatlogo1.png").convert_alpha()
img=pygame.image.load("flame.png").convert()
l1=[0 for x in range(200)]
blank=[(255,255,255) for x in range(200)]
anim_color=[(255,255,255),(255,0,0),(0,255,0),(99,115,255)]
f=pygame.font.SysFont("comicsans",30)
def draw_grid():
    for x in range(1,200):
        blank[x]=anim_color[0]
        l1[x]=random.randrange(1,100)
draw_grid()#draws base
def redrawWindow():
    surf.fill((0,0,0))
    draw()
    pygame.display.update()
    pygame.time.delay(10)

def draw():
    global sort
    #text=f.render("WELCOME",1,(255,255,255))
    #surf.blit(text,(20,20))
    surf.blit(img,(0,0))
    text=f.render("Press ENTER to sort and R to make a new array and C to cycle sorting methods",1,(255,255,255))
    surf.blit(text,(10, 20))
    t="Currently using {} sort".format(sort)
    text=f.render(t,1,(255,255,255))
    surf.blit(text,(W-300, 45))
    #surf.blit(pic,(5,200))
    barW=(W-50)//200
    boundary_l1=900/200
    boundary_grp=600/100
    #pygame.draw.line(surf,(255,255,255),(0,95),(900,95),6)
    pygame.draw.line(surf,(255,255,255),(42,95),(950,95),6)
    for x in range(1,100):
        pygame.draw.line(surf,(0,0,0),(42,boundary_grp*x+100),\
                         (900,boundary_grp*x+100),1)
    for x in range(1,200):
        pygame.draw.line(surf,blank[x],\
                         (boundary_l1*x-3+42,100),\
                         (boundary_l1*x-3+42,l1[x]*boundary_grp+100),barW)
    #surf.blit(pic,(5,150))
    

def merge_sort(l1,l,r):
    midpoint=(l+r)//2
    if l<r:
        merge_sort(l1,l,midpoint)
        merge_sort(l1,midpoint+1,r)
        merge(l1,l,midpoint,midpoint+1,r)
def merge(l1,x1,y1,x2,y2):
    temp=[]
    q=x1
    w=x2
    #pygame.event.pump()
    while q<=y1 and w<=y2:
        blank[q]=anim_color[1]
        blank[w]=anim_color[1]
        redrawWindow()
        blank[q]=anim_color[0]
        blank[w]=anim_color[0]
        if l1[q]<l1[w]:
            temp.append(l1[q])
            q=q+1
        else:
            temp.append(l1[w])
            w=w+1
    while q<=y1:
        blank[q]=anim_color[1]
        redrawWindow()
        blank[q]=anim_color[0]
        temp.append(l1[q])
        q=q+1
    while w<=y2:
        blank[w]=anim_color[1]
        redrawWindow()
        blank[w]=anim_color[0]
        w=w+1
    w=0
    for q in range(x1,y2+1):
        #print(temp,w)
        pygame.event.pump()#fixes crashing
        if w<len(temp):
            #pygame.event.pump()
            l1[q]=temp[w]
            w=w+1
            blank[q]=anim_color[2]
            redrawWindow()
            if y2-x1==len(l1)-2:
                blank[q]=anim_color[3]
            else:
                blank[q]=anim_color[0]
def bubble_sort(nums):
    i=0
    numslen=len(nums)
    fl=True
    while i<numslen and fl==True:
        fl=False
        for l in range(numslen-i-1):
            if nums[l]>nums[l+1]:
                pygame.event.pump()
                t=nums[l]
                nums[l]=nums[l+1]
                nums[l+1]=t
                blank[l]=anim_color[1]
                redrawWindow()
                blank[l]=anim_color[0]
                fl=True
        i=i+1
def insertion_sort(nums):
    #i=1
    numslen=len(nums)
    for i in range(numslen):
        pygame.event.pump()
        cv=nums[i]
        blank[i]=anim_color[1]
        redrawWindow()
        blank[i]=anim_color[0]
        p=i
        while p>0 and nums[p-1]>cv:
            nums[p]=nums[p-1]
            p=p-1
        nums[p]=cv
        blank[p]=anim_color[1]
        redrawWindow()
        blank[p]=anim_color[0]
def partition(nums,start,end):
    pivot=nums[start]
    blank[pivot]=anim_color[2]
    lm=start+1
    rm=end
    done=False
    while done==False:
        pygame.event.pump()
        blank[pivot]=anim_color[2]
        while lm<=rm and nums[lm]<=pivot:
            lm=lm+1
            blank[lm]=anim_color[1]
            redrawWindow()
            blank[lm]=anim_color[0]
        while nums[rm]>=pivot and rm>=lm:
            rm=rm-1
            blank[rm]=anim_color[1]
            redrawWindow()
            blank[rm]=anim_color[0]
        if rm<lm:
            done=True
        else:
            temp=nums[lm]
            nums[lm]=nums[rm]
            nums[rm]=temp
            
    temp=nums[start]
    nums[start]=nums[rm]
    nums[rm]=temp
    return rm

def quick_sort(nums,start,end):
    if start<end:
        split=partition(nums,start,end)
        quick_sort(nums,start,split-1)
        quick_sort(nums,split+1,end)
def cycle():
    global sortpoint
    global sort
    sortlist=['merge','bubble','insertion','quick']
    if sortpoint!=len(sortlist)-1:
        sortpoint+=1
        sort=sortlist[sortpoint]
        return sort
    else:
        sortpoint=0
        sort=sortlist[sortpoint]
        return sort
        
while run:
        # background 
    surf.fill((0, 0, 0))
    # Event handler stores all event  
    for event in pygame.event.get(): 
        # If we click Close button in window 
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                draw_grid()  
            if event.key == pygame.K_RETURN: 
                #merge_sort(l1,1,len(l1)-1)
                if sort=='bubble':
                    bubble_sort(l1)
                elif sort=='merge':
                    merge_sort(l1,1,len(l1)-1)
                elif sort=='insertion':
                    insertion_sort(l1)
                elif sort=='quick':
                    quick_sort(l1,1,len(l1)-1)
            if event.key==pygame.K_c:
                cycle()
    draw() 
    pygame.display.flip() 
     
pygame.quit() 
    
